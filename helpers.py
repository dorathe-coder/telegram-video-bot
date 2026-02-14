#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper functions for video downloading and processing
"""

import os
import re
import asyncio
import logging
from typing import List, Dict, Optional
from yt_dlp import YoutubeDL
from config import Config

logger = logging.getLogger(__name__)


def extract_links_from_txt(file_path: str) -> List[Dict[str, str]]:
    """
    Extract video links from text file
    
    Supported formats:
    1. Title:URL (Classplus format)
    2. Title: URL
    3. https://youtube.com/watch?v=xxxxx
       Title: My Video Title
    4. Just URLs
    """
    links = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split by lines
        lines = content.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            
            if not line or line.startswith('#'):
                continue
            
            # Format 1: Title:URL (Classplus style)
            if ':https://' in line or ':http://' in line:
                parts = line.split(':', 1)
                if len(parts) == 2 and parts[1].startswith('http'):
                    # Find the actual URL part
                    url_start = line.find('http')
                    title = line[:url_start-1].strip()
                    url = line[url_start:].strip()
                    
                    links.append({
                        'url': url,
                        'title': title or f'Video_{len(links) + 1}'
                    })
                    continue
            
            # Format 2: Just URL
            if line.startswith('http://') or line.startswith('https://'):
                links.append({
                    'url': line,
                    'title': f'Video_{len(links) + 1}'
                })
        
        # Fallback: Extract all URLs if no links found
        if not links:
            current_url = None
            current_title = None
            
            for line in lines:
                line = line.strip()
                
                # Check if line is a URL
                if re.match(r'https?://', line):
                    # Save previous entry if exists
                    if current_url:
                        links.append({
                            'url': current_url,
                            'title': current_title or f'Video_{len(links) + 1}'
                        })
                    
                    current_url = line
                    current_title = None
                
                # Check if line is a title
                elif line.lower().startswith('title:'):
                    current_title = line.split(':', 1)[1].strip()
                
                # If line contains both URL and might be title on same line
                elif current_url and line and not line.startswith('#'):
                    if not current_title:
                        current_title = line
            
            # Add last entry
            if current_url:
                links.append({
                    'url': current_url,
                    'title': current_title or f'Video_{len(links) + 1}'
                })
        
        # Final fallback: regex extraction
        if not links:
            urls = re.findall(r'https?://[^\s]+', content)
            links = [{'url': url, 'title': f'Video_{i+1}'} for i, url in enumerate(urls)]
        
        logger.info(f"Extracted {len(links)} links from {file_path}")
        return links
        
    except Exception as e:
        logger.error(f"Error extracting links: {str(e)}")
        return []


def sanitize_filename(filename: str) -> str:
    """Sanitize filename by removing invalid characters"""
    # Remove invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    # Limit length
    if len(filename) > 200:
        filename = filename[:200]
    return filename


async def download_video(url: str, quality: str = "720", progress_message=None) -> Optional[str]:
    """
    Download video using yt-dlp
    Supports M3U8/HLS streams including Classplus encrypted links
    
    Args:
        url: Video URL
        quality: Video quality (360/480/720/1080)
        progress_message: Telegram message for progress updates
    
    Returns:
        Path to downloaded video file or None if failed
    """
    try:
        # Prepare download options
        quality_format = Config.QUALITY_OPTIONS.get(quality, Config.QUALITY_OPTIONS["720"])
        
        # Output template
        output_template = os.path.join(Config.DOWNLOAD_PATH, '%(title)s.%(ext)s')
        
        ydl_opts = {
            'format': quality_format,
            'outtmpl': output_template,
            'merge_output_format': 'mp4',
            'quiet': True,
            'no_warnings': True,
            
            # M3U8/HLS stream support
            'hls_prefer_native': True,
            'hls_use_mpegts': True,
            
            # Download settings
            'concurrent_fragment_downloads': 5,
            'retries': 10,
            'fragment_retries': 10,
            'socket_timeout': 30,
            'http_chunk_size': 10485760,  # 10MB
            
            # External downloader (faster for streams)
            'external_downloader': 'ffmpeg',
            'external_downloader_args': [
                '-loglevel', 'quiet',
                '-stats',
                '-protocol_whitelist', 'file,http,https,tcp,tls,crypto'
            ],
            
            # Post-processing
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            
            # Headers for encrypted streams (Classplus, etc.)
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Referer': 'https://web.classplusapp.com/',
                'Origin': 'https://web.classplusapp.com',
            },
            
            # Allow extraction from encrypted platforms
            'nocheckcertificate': True,
            'allow_unplayable_formats': False,
            'ignoreerrors': False,
        }
        
        # Add progress hook
        if progress_message:
            def progress_hook(d):
                if d['status'] == 'downloading':
                    try:
                        percentage = d.get('_percent_str', '0%')
                        speed = d.get('_speed_str', 'N/A')
                        eta = d.get('_eta_str', 'N/A')
                        
                        asyncio.create_task(
                            progress_message.edit_text(
                                f"📥 **Downloading...**\n\n"
                                f"Progress: {percentage}\n"
                                f"Speed: {speed}\n"
                                f"ETA: {eta}"
                            )
                        )
                    except:
                        pass
            
            ydl_opts['progress_hooks'] = [progress_hook]
        
        # Download video
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            
            # Get downloaded file path
            if info:
                title = sanitize_filename(info.get('title', 'video'))
                file_path = os.path.join(Config.DOWNLOAD_PATH, f"{title}.mp4")
                
                # Check if file exists
                if os.path.exists(file_path):
                    # Check file size
                    file_size = os.path.getsize(file_path)
                    
                    if file_size > Config.MAX_FILE_SIZE:
                        os.remove(file_path)
                        raise Exception(f"File size ({file_size / (1024**3):.2f} GB) exceeds limit (2 GB)")
                    
                    logger.info(f"Downloaded: {file_path} ({file_size / (1024**2):.2f} MB)")
                    return file_path
                
                # Try alternative extensions
                for ext in ['mkv', 'webm', 'mp4', 'ts']:
                    alt_path = os.path.join(Config.DOWNLOAD_PATH, f"{title}.{ext}")
                    if os.path.exists(alt_path):
                        # Convert to mp4 if needed
                        if ext != 'mp4':
                            new_path = os.path.join(Config.DOWNLOAD_PATH, f"{title}.mp4")
                            os.rename(alt_path, new_path)
                            return new_path
                        return alt_path
        
        return None
        
    except Exception as e:
        logger.error(f"Error downloading {url}: {str(e)}")
        
        if progress_message:
            try:
                await progress_message.edit_text(f"❌ Download failed: {str(e)}")
            except:
                pass
        
        return None


def get_video_info(url: str) -> Optional[Dict]:
    """
    Get video information without downloading
    
    Args:
        url: Video URL
    
    Returns:
        Video information dict or None
    """
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            if info:
                return {
                    'title': info.get('title', 'Unknown'),
                    'duration': info.get('duration', 0),
                    'uploader': info.get('uploader', 'Unknown'),
                    'thumbnail': info.get('thumbnail', ''),
                    'description': info.get('description', '')[:500],
                    'view_count': info.get('view_count', 0),
                    'like_count': info.get('like_count', 0),
                }
        
        return None
        
    except Exception as e:
        logger.error(f"Error getting video info: {str(e)}")
        return None


def cleanup_downloads():
    """Clean up download directory"""
    try:
        if os.path.exists(Config.DOWNLOAD_PATH):
            for file in os.listdir(Config.DOWNLOAD_PATH):
                file_path = os.path.join(Config.DOWNLOAD_PATH, file)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    logger.error(f"Error deleting {file_path}: {str(e)}")
        
        logger.info("Download directory cleaned up")
    except Exception as e:
        logger.error(f"Error cleaning up downloads: {str(e)}")


# Supported platforms (for reference)
SUPPORTED_PLATFORMS = [
    "YouTube", "Vimeo", "Dailymotion", "Instagram", "Facebook",
    "Twitter", "TikTok", "Reddit", "Twitch", "SoundCloud",
    "Classplus", "Apna College", "Unacademy", "Physics Wallah",
    "And 1000+ more platforms supported by yt-dlp"
]
