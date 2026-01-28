from telegram.ext import Updater, CommandHandler
from config import BOT_TOKEN

def start(update, context):
    update.message.reply_text("Welcome! Use /subscribe or /trial.")

updater = Updater(BOT_TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()