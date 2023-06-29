import telegram
from telegram.ext import Updater, MessageHandler, Filters

import config
import manufact_data


api_token = config.TELEGRAM_BOT_API
chat_id = config.TELEGRAM_BOT_CHAT_API

bot = telegram.Bot(api_token)
updater = Updater(api_token, use_context=True)
dispatcher = updater.dispatcher

def send_message():
    bot.sendMessage(chat_id=chat_id, text="3일 내 실적발표 기업들입니다.")
    for row in manufact_data.sort_close_earnings():
        bot.sendMessage(
            chat_id=chat_id, 
            text=f"Ticker(종목코드): {row[0]} 종목명: {row[1]} 실적발표: {row[2]}"
            )
    bot.sendMessage(chat_id=chat_id, text="집중관찰하고 싶은 종목코드를 ,로 구분하여 작성해주세요.")
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    
# asyncio.run(send_message())

def echo(update, context):
    user_text = update.message.text.split(',')
    user_management = [element.replace(' ','') for element in user_text]
    print(user_management)
    for row in user_management:
        print(row)
    
    return user_management

send_message()