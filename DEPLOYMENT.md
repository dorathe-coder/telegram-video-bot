# 🚀 Complete Deployment Guide

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Render Deployment (Recommended)](#render-deployment)
3. [Railway Deployment](#railway-deployment)
4. [Koyeb Deployment](#koyeb-deployment)
5. [Local Testing](#local-testing)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### 1. Get Telegram API Credentials

**Step 1:** Go to https://my.telegram.org
**Step 2:** Login with your phone number
**Step 3:** Click on "API Development Tools"
**Step 4:** Fill the form:
- App title: `My Video Bot` (any name)
- Short name: `videobot` (any short name)
- Platform: Choose any
- Description: Optional

**Step 5:** Copy these values:
- `api_id` → This is your **API_ID**
- `api_hash` → This is your **API_HASH**

Example:
```
API_ID: 31708653
API_HASH: 618773cba18e732111276d01571a928f
```

### 2. Create Telegram Bot

**Step 1:** Open Telegram and search for [@BotFather](https://t.me/BotFather)

**Step 2:** Send `/newbot` command

**Step 3:** Follow instructions:
- Bot name: `My Video Downloader Bot` (any name)
- Bot username: `myvideo_dl_bot` (must be unique, end with 'bot')

**Step 4:** Copy the bot token

Example:
```
BOT_TOKEN: YOUR_BOT_TOKEN_HERE
```

### 3. Get Your User ID

**Step 1:** Open Telegram and search for [@userinfobot](https://t.me/userinfobot)

**Step 2:** Send any message or `/start`

**Step 3:** Copy your user ID

Example:
```
OWNER_ID: 123456789
```

### 4. MongoDB (Optional but Recommended)

**Step 1:** Go to https://www.mongodb.com/cloud/atlas

**Step 2:** Sign up for free account

**Step 3:** Create a free cluster (M0 Sandbox - FREE forever)

**Step 4:** Create database user:
- Username: `botuser`
- Password: `strongpassword123`

**Step 5:** Add IP to whitelist:
- Click "Network Access"
- Add IP: `0.0.0.0/0` (allow from anywhere)

**Step 6:** Get connection string:
- Click "Connect" → "Connect your application"
- Copy the connection string
- Replace `<password>` with your password

Example:
```
MONGODB_URI: mongodb+srv://username:password@cluster.mongodb.net/...
```

---

## Render Deployment (Recommended - 100% Free)

### Why Render?
- ✅ 750 hours/month FREE
- ✅ Auto-deploy from GitHub
- ✅ Easy environment variables
- ✅ Good for 24/7 bots
- ✅ No credit card required

### Step-by-Step Guide

#### Step 1: Fork Repository

1. Go to this GitHub repository
2. Click **"Fork"** button (top right)
3. This creates your own copy

#### Step 2: Sign Up on Render

1. Go to https://render.com
2. Click **"Get Started"**
3. Sign up with **GitHub** (recommended)
4. Authorize Render to access your repositories

#### Step 3: Create Web Service

1. Click **"New +"** button
2. Select **"Web Service"**
3. Click **"Connect a repository"**
4. Find and select your forked repository
5. Click **"Connect"**

#### Step 4: Configure Service

Fill in these settings:

**Basic Settings:**
- **Name**: `telegram-video-bot` (or any unique name)
- **Region**: Choose closest to you
- **Branch**: `main`
- **Root Directory**: Leave empty
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python bot.py`

**Instance Type:**
- Select **"Free"** (gives 750 hours/month)

#### Step 5: Add Environment Variables

Click **"Advanced"** button, then add these:

**Required Variables:**
```bash
API_ID = 31708653
API_HASH = 618773cba18e732111276d01571a928f
BOT_TOKEN = YOUR_BOT_TOKEN_HERE
OWNER_ID = 123456789  # YOUR USER ID
```

**Optional Variables:**
```bash
DEVELOPER_NAME = Your Name
SUPPORT_CONTACT = @yourusername
MONGODB_URI = mongodb+srv://...
AUTH_USERS = 111111111,222222222
ENABLE_PUBLIC_USE = True
```

**How to add:**
1. Click **"Add Environment Variable"**
2. Enter **Key** (e.g., `API_ID`)
3. Enter **Value** (e.g., `31708653`)
4. Click **"Add"**
5. Repeat for all variables

#### Step 6: Deploy!

1. Click **"Create Web Service"**
2. Wait 5-10 minutes for build
3. Check logs for "🚀 Bot starting..."
4. Status should show "Live"

#### Step 7: Test Your Bot

1. Open Telegram
2. Search for your bot username
3. Send `/start`
4. Bot should respond!

---

## Railway Deployment

### Why Railway?
- ✅ $5 free credit/month
- ✅ Very easy deployment
- ✅ Good interface
- ⚠️ Requires credit card verification

### Step-by-Step Guide

#### Step 1: Sign Up

1. Go to https://railway.app
2. Sign up with GitHub
3. Verify email

#### Step 2: Create Project

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Select your forked repository

#### Step 3: Add Environment Variables

1. Click on your service
2. Go to **"Variables"** tab
3. Add all environment variables (same as Render)

#### Step 4: Deploy

1. Railway auto-deploys
2. Check logs
3. Test bot!

---

## Koyeb Deployment

### Why Koyeb?
- ✅ Free tier available
- ✅ Good for global deployment
- ✅ Fast deployment

### Step-by-Step Guide

#### Step 1: Sign Up

1. Go to https://www.koyeb.com
2. Sign up with GitHub

#### Step 2: Create App

1. Click **"Create App"**
2. Select **"GitHub"**
3. Choose your repository

#### Step 3: Configure

1. Set environment variables
2. Set start command: `python bot.py`
3. Deploy!

---

## Local Testing (Windows/Mac/Linux)

### Windows

```bash
# Install Python 3.11+ from python.org

# Clone repository
git clone https://github.com/yourusername/telegram-video-bot.git
cd telegram-video-bot

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env
# Edit .env with your credentials

# Run bot
python bot.py
```

### Mac/Linux

```bash
# Install Python 3.11+
# On Ubuntu: sudo apt install python3.11 python3-pip

# Clone repository
git clone https://github.com/yourusername/telegram-video-bot.git
cd telegram-video-bot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install system dependencies
sudo apt install ffmpeg aria2  # Ubuntu/Debian
brew install ffmpeg aria2      # macOS

# Create .env file
cp .env.example .env
# Edit .env with your credentials

# Run bot
python bot.py
```

---

## Troubleshooting

### Common Issues

#### 1. "Invalid API_ID or API_HASH"

**Solution:**
- Double-check your API_ID and API_HASH
- Make sure there are no extra spaces
- Get new credentials from https://my.telegram.org

#### 2. "Bot token is invalid"

**Solution:**
- Get a new token from @BotFather
- Make sure token is complete (no spaces)
- Don't share token publicly

#### 3. Bot not responding

**Solution:**
- Check if bot is running (Render dashboard)
- Check logs for errors
- Make sure OWNER_ID is set correctly
- Test with `/start` command

#### 4. Download fails

**Solution:**
- Check if platform is supported
- Try different quality setting
- Check URL format
- Some platforms need authentication

#### 5. Upload fails

**Solution:**
- File might be >2GB (Telegram limit)
- Use lower quality (480p or 720p)
- Check internet connection

#### 6. "Not authorized" error

**Solution:**
- Set OWNER_ID correctly
- Add your ID to AUTH_USERS
- Or set ENABLE_PUBLIC_USE=True

#### 7. Render service keeps stopping

**Solution:**
- Check free tier hours (750/month)
- Make sure all dependencies installed
- Check logs for errors
- Bot might be using too much memory

#### 8. MongoDB connection error

**Solution:**
- Check connection string
- Whitelist all IPs (0.0.0.0/0)
- Make sure cluster is running
- Optional: Bot works without MongoDB

---

## Monitoring

### Render Dashboard

1. Go to https://dashboard.render.com
2. Click on your service
3. View:
   - Logs (real-time)
   - Metrics (CPU, Memory)
   - Events (deploys, restarts)

### Bot Commands

```bash
/stats  # View bot statistics (owner only)
```

### Checking Logs

**Render:**
- Dashboard → Your Service → Logs

**Railway:**
- Project → Deployments → View Logs

**Local:**
- Console output

---

## Updating Bot

### On Render (auto-deploy enabled):

1. Make changes to code
2. Commit and push to GitHub
3. Render auto-deploys
4. Check logs

### Manual Deploy:

1. Render Dashboard
2. Your Service
3. "Manual Deploy"
4. Click "Deploy latest commit"

---

## Best Practices

1. **Security:**
   - Never commit .env file
   - Use environment variables
   - Don't share bot token

2. **Performance:**
   - Use 720p for best balance
   - Clean up downloads regularly
   - Monitor resource usage

3. **User Experience:**
   - Set custom captions
   - Use thumbnails
   - Provide clear error messages

4. **Maintenance:**
   - Check logs regularly
   - Update dependencies
   - Monitor free tier limits

---

## Need Help?

- 📧 Email: support@example.com
- 💬 Telegram: @yourusername
- 🐛 Issues: GitHub Issues
- 📖 Docs: README.md

---

## Quick Reference

### Environment Variables

| Variable | Example | Required |
|----------|---------|----------|
| API_ID | 31708653 | ✅ |
| API_HASH | 618773cba... | ✅ |
| BOT_TOKEN | 8270366317:AAE... | ✅ |
| OWNER_ID | 123456789 | ✅ |
| MONGODB_URI | mongodb+srv://... | ❌ |
| AUTH_USERS | 111,222,333 | ❌ |
| DEVELOPER_NAME | Your Name | ❌ |

### Commands

| Command | Description | Access |
|---------|-------------|--------|
| /start | Start bot | All |
| /help | Get help | All |
| /settings | Configure | All |
| /stats | Statistics | Owner |
| /broadcast | Message all | Owner |

---

**Happy Deploying! 🚀**
