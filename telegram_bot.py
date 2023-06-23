import telegram
from telegram.ext import Updater
import asyncio
import config


api_token = config.telegram_bot_api
chat_id = config.telegram_bot_chat_id

bot = telegram.Bot(token = api_token)
asyncio.run(bot.sendMessage(chat_id = chat_id, text="테스트"))

# updater
updater = Updater(token=api_token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

