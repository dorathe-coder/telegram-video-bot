#!/bin/bash

# Telegram Video Bot Startup Script

echo "🚀 Starting Telegram Video Bot..."

# Create necessary directories
mkdir -p downloads
mkdir -p logs

# Install system dependencies (for Render/Railway/Koyeb)
if command -v apt-get &> /dev/null; then
    echo "📦 Installing system dependencies..."
    apt-get update -qq
    apt-get install -y -qq ffmpeg aria2 > /dev/null 2>&1
    echo "✅ FFmpeg and aria2 installed"
fi

# For Alpine Linux (some hosting platforms)
if command -v apk &> /dev/null; then
    echo "📦 Installing system dependencies (Alpine)..."
    apk add --no-cache ffmpeg aria2
fi

# Install Python dependencies
echo "📦 Installing Python packages..."
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet

# Verify FFmpeg installation
if command -v ffmpeg &> /dev/null; then
    echo "✅ FFmpeg is ready"
else
    echo "⚠️  FFmpeg not found - video processing may fail"
fi

# Check configuration
echo "⚙️ Validating configuration..."
python -c "from config import Config; Config.validate()" || {
    echo "❌ Configuration validation failed!"
    echo "Please set: API_ID, API_HASH, BOT_TOKEN, OWNER_ID"
    exit 1
}

# Start the bot
echo "✅ Starting bot..."
python bot.py
