
from telegram import Bot
from telegram.ext import Updater, CommandHandler

token1 = ' '
bot = Bot(token= token1)
updater = Updater(token= token1)
dispatcher = updater.dispatcher

def erase_words(update, context):
    words = update.message.text[6:]
    context.bot.send_message(
        update.effective_chat.id,
        f"{' '.join(filter(lambda word:'абв' not in word.lower(), words.split()))}"
    )

start_handler = CommandHandler('start', erase_words)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()

# Отправлять в формате "/start текст"