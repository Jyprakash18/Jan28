import os

BOT_TOKEN = os.getenv('BOT_TOKEN')  # From Telegram BotFather
RAZORPAY_KEY_ID = os.getenv('RAZORPAY_KEY_ID')
RAZORPAY_KEY_SECRET = os.getenv('RAZORPAY_KEY_SECRET')
DATABASE_URL = os.getenv('DATABASE_URL')  # For user subscriptions (e.g., PostgreSQL on Render)
CHANNEL_ID = os.getenv('CHANNEL_ID')  # Telegram channel/group ID for add/remove
TRIAL_DAYS = 7  # Free trial duration