import telegram
from telegram.ext import Updater, MessageHandler, Filters
import asyncio
import config as config
import result


api_token = config.telegram_bot_api
chat_id = config.telegram_bot_chat_id

bot = telegram.Bot(api_token)

updater = Updater(api_token, use_context=True)
dispatcher = updater.dispatcher

async def send_message():
    bot.sendMessage(chat_id=chat_id, text=f"금주 실적발표 기업들입니다.")
    for row in result.sort_close_earnings():
        await bot.sendMessage(
            chat_id=chat_id, 
            text=f"Ticker(종목코드): {row[0]} 종목명: {row[1]} 실적발표: {row[2]}")
    
# asyncio.run(send_message())

def echo(update, context):
    user_text = update.message.text
    context.bot.send_message(chat_id=chat_id, text=user_text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

dispatcher.add_handler(echo_handler)

updater.start_polling()