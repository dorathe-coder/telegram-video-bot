# 🎥 Universal Telegram Video Downloader Bot

A powerful Telegram bot that downloads videos from 1000+ platforms including YouTube, Classplus, Appx, and encrypted educational platforms.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

## 🌟 Features

### Core Features
- ✅ **Universal Support**: Download from YouTube, Vimeo, Instagram, Facebook, Twitter, Classplus, Apna College, and 1000+ platforms
- ✅ **Batch Processing**: Process multiple links from a single text file
- ✅ **High-Speed Downloads**: Concurrent downloading with aria2c
- ✅ **Auto Upload**: Direct upload to Telegram chats or channels
- ✅ **Custom Thumbnails**: Set custom thumbnails for all videos
- ✅ **Custom Captions**: Personalized captions with variables
- ✅ **Multiple Quality Options**: 360p, 480p, 720p, 1080p

### Management Features
- ✅ **Authorization System**: Control who can use the bot
- ✅ **Owner Commands**: Broadcast, statistics, user management
- ✅ **Progress Tracking**: Real-time download/upload progress
- ✅ **Auto Cleanup**: Automatic temporary file deletion
- ✅ **Logs & Stats**: Track usage and performance

### Deployment
- ✅ **100% Free Hosting**: Deploy on Render.com (750 hours/month free)
- ✅ **One-Click Deploy**: Simple setup process
- ✅ **Auto Updates**: GitHub integration for updates
- ✅ **No Credit Card Required**: Completely free

---

## 🚀 Quick Start Guide

### Prerequisites

You need to gather these before deployment:

1. **Telegram API Credentials**
   - Go to https://my.telegram.org
   - Login with your phone number
   - Click on "API Development Tools"
   - Copy `API ID` and `API Hash`

2. **Bot Token**
   - Message [@BotFather](https://t.me/BotFather) on Telegram
   - Send `/newbot` command
   - Follow instructions to create bot
   - Copy the bot token

3. **Your Telegram User ID**
   - Message [@userinfobot](https://t.me/userinfobot)
   - Copy your user ID

4. **MongoDB (Optional - for user tracking)**
   - Go to https://www.mongodb.com/cloud/atlas
   - Create free account (M0 Sandbox)
   - Create cluster
   - Get connection string

---

## 📦 Deployment Guide

### Method 1: Deploy to Render (Recommended - 100% Free)

#### Step 1: Fork this Repository
1. Click the **Fork** button at the top right
2. This creates your own copy of the repository

#### Step 2: Sign Up on Render
1. Go to https://render.com
2. Sign up using your **GitHub account**
3. Authorize Render to access your repositories

#### Step 3: Create New Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect your forked repository
3. Configure:
   - **Name**: `telegram-video-bot` (or any name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
   - **Instance Type**: `Free`

#### Step 4: Add Environment Variables
Click **"Advanced"** and add these environment variables:

```bash
API_ID = YOUR_API_ID
API_HASH = YOUR_API_HASH
BOT_TOKEN = YOUR_BOT_TOKEN
OWNER_ID = YOUR_TELEGRAM_USER_ID
DEVELOPER_NAME = Your Name
SUPPORT_CONTACT = @yourusername
```

**Optional Variables:**
```bash
MONGODB_URI = YOUR_MONGODB_URI
AUTH_USERS = 123456789,987654321
ENABLE_PUBLIC_USE = True
```

#### Step 5: Deploy
1. Click **"Create Web Service"**
2. Wait 5-10 minutes for deployment
3. Check logs for "🚀 Bot starting..."
4. Test your bot on Telegram!

---

### Method 2: Deploy to Railway

1. Go to https://railway.app
2. Sign up with GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Select your forked repository
5. Add environment variables (same as above)
6. Deploy!

---

### Method 3: Deploy to Koyeb

1. Go to https://www.koyeb.com
2. Sign up and create new app
3. Select **"GitHub"** deployment
4. Choose your repository
5. Add environment variables
6. Deploy!

---

## 📝 How to Use the Bot

### For Users

1. **Start the bot**
   ```
   /start
   ```

2. **Send a text file** with video links:
   ```
   https://youtube.com/watch?v=xxxxx
   Title: My First Video

   https://vimeo.com/xxxxx
   Title: My Second Video
   ```

3. **Or send direct link**:
   ```
   https://youtube.com/watch?v=xxxxx
   ```

4. **Configure settings**:
   ```
   /settings
   ```

### Text File Format

**Simple format (just URLs):**
```
https://youtube.com/watch?v=xxxxx
https://vimeo.com/xxxxx
https://dailymotion.com/video/xxxxx
```

**Advanced format (with titles):**
```
https://youtube.com/watch?v=xxxxx
Title: Introduction to Python

https://vimeo.com/xxxxx
Title: Advanced JavaScript Concepts

https://classplus.co/course/xxxxx
Title: Physics Chapter 1
```

### Available Commands

**User Commands:**
- `/start` - Start the bot
- `/help` - Get detailed help
- `/settings` - Configure bot settings
- `/stats` - View statistics (if enabled)
- `/about` - About the bot

**Owner Commands:**
- `/broadcast <message>` - Send message to all users
- `/stats` - Detailed bot statistics
- `/add_user <user_id>` - Authorize a user
- `/remove_user <user_id>` - Deauthorize a user

### Settings Options

**Thumbnail:**
- Set custom thumbnail for videos
- Remove thumbnail

**Channel:**
- Set upload channel (bot must be admin)
- Remove channel (uploads to DM)

**Caption:**
- Set custom caption template
- Use variables: `{title}`, `{index}`
- Example: `🎬 {title} - Video #{index}`

**Quality:**
- 360p - Low quality, small file size
- 480p - Medium quality
- 720p - HD quality (recommended)
- 1080p - Full HD quality (large files)

---

## 🛠️ Configuration

### config.py Variables

Edit `config.py` or set environment variables:

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `API_ID` | Telegram API ID | - | ✅ Yes |
| `API_HASH` | Telegram API Hash | - | ✅ Yes |
| `BOT_TOKEN` | Bot token from BotFather | - | ✅ Yes |
| `OWNER_ID` | Your Telegram user ID | 0 | ✅ Yes |
| `DEVELOPER_NAME` | Your name | "Your Name" | ❌ No |
| `SUPPORT_CONTACT` | Your username | "@yourusername" | ❌ No |
| `MONGODB_URI` | MongoDB connection string | "" | ❌ No |
| `AUTH_USERS` | Authorized user IDs (comma-separated) | "" | ❌ No |
| `ENABLE_PUBLIC_USE` | Allow public use | True | ❌ No |

---

## 🎯 Supported Platforms

The bot supports **1000+ platforms** using yt-dlp, including:

**Video Platforms:**
- YouTube, YouTube Music
- Vimeo, Dailymotion
- Instagram, Facebook, Twitter
- TikTok, Reddit, Twitch
- SoundCloud, Mixcloud

**Educational Platforms:**
- Classplus
- Apna College
- Unacademy
- Physics Wallah
- Khan Academy
- Coursera (public videos)
- Udemy (preview videos)

**Indian Platforms:**
- Hotstar
- Zee5
- SonyLIV
- Voot
- MX Player
- JioCinema

And many more! Full list: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

---

## 🔒 Security & Privacy

- ✅ All downloads are temporary and auto-deleted
- ✅ No data is stored permanently (unless MongoDB enabled)
- ✅ Session files are gitignored
- ✅ Environment variables for sensitive data
- ✅ Authorization system to control access

---

## 📊 Features in Detail

### Batch Processing
- Process up to 50 links in one text file
- Automatic title extraction
- Sequential processing with progress updates
- Error handling for failed downloads

### Custom Thumbnails
1. Send `/settings`
2. Click "Set Thumbnail"
3. Send an image
4. Thumbnail will be applied to all videos

### Channel Posting
1. Add bot as admin to your channel
2. Send `/settings`
3. Click "Set Channel"
4. Send channel username (e.g., `@mychannel`)
5. All videos will be posted to channel

### Quality Selection
- **360p**: ~50-100 MB per hour
- **480p**: ~200-300 MB per hour
- **720p**: ~500-800 MB per hour (recommended)
- **1080p**: ~1-2 GB per hour (may exceed Telegram limit)

---

## 🐛 Troubleshooting

### Bot not responding?
- Check if bot is running in Render dashboard
- Check logs for errors
- Verify BOT_TOKEN is correct

### Downloads failing?
- Check if the platform is supported
- Try different quality settings
- Check Render logs for specific errors

### Upload errors?
- File might be too large (>2GB Telegram limit)
- Try lower quality
- Check if bot has permission in channel

### "Not authorized" error?
- Add your user ID to `OWNER_ID`
- Or add to `AUTH_USERS` environment variable
- Restart the bot

---

## 💡 Tips & Tricks

1. **Faster Downloads**: Bot uses aria2c for concurrent downloads
2. **Save Bandwidth**: Use 480p or 720p quality
3. **Organize Videos**: Use custom captions with numbering
4. **Bulk Processing**: Prepare text files with organized links
5. **Channel Backup**: Set a private channel for all downloads

---

## 🔄 Updating the Bot

### On Render:
1. Push changes to your GitHub repository
2. Render auto-deploys (if auto-deploy enabled)
3. Or manually click "Deploy latest commit"

### Manual Update:
1. Git pull latest changes
2. Restart the bot service

---

## 📈 Monitoring

### Render Dashboard:
- View real-time logs
- Monitor resource usage
- Check uptime status
- Restart service if needed

### Bot Commands:
- `/stats` - View usage statistics (owner only)
- Check logs for errors and warnings

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License.

---

## ⚠️ Disclaimer

This bot is for **educational purposes only**. 

- Respect copyright laws
- Follow platform terms of service
- Don't use for piracy or illegal content
- Educational content downloading should comply with fair use

---

## 🙏 Credits

- **yt-dlp**: https://github.com/yt-dlp/yt-dlp
- **Pyrogram**: https://github.com/pyrogram/pyrogram
- **Render**: https://render.com
- **Developer**: [Your Name]

---

## 📞 Support

Need help? 

- 📧 Contact: {SUPPORT_CONTACT}
- 🐛 Issues: GitHub Issues
- 💬 Telegram: @yourusername

---

## 🎉 Enjoy!

If you find this bot useful, please:
- ⭐ Star this repository
- 🔄 Share with friends
- 🐛 Report bugs
- 💡 Suggest features

---

Made with ❤️ by {DEVELOPER_NAME}
