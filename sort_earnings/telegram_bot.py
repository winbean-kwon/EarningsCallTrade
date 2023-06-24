import telegram
from telegram.ext import Updater
import asyncio
import config as config
import result


async def send_message():
    api_token = config.telegram_bot_api
    chat_id = config.telegram_bot_chat_id

    bot = telegram.Bot(token = api_token)

    bot.sendMessage(chat_id=chat_id, text=f"금주 실적발표 기업들입니다.")
    for row in result.sort_close_earnings():
        await bot.sendMessage(
            chat_id=chat_id, 
            text=f"Ticker(종목코드): {row[0]} 종목명: {row[1]} 실적발표: {row[2]}")
    
    # updater
    updater = Updater(token=api_token, use_context=True)
    dispatcher = updater.dispatcher
    updater.start_polling()

asyncio.run(send_message())