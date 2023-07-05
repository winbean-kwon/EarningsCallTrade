'''telegram bot'''
from typing import List
import csv
import telegram
from telegram.ext import Updater, MessageHandler, Filters

import config
import manufact_data


api_token: str = config.TELEGRAM_BOT_API
chat_id: str = config.TELEGRAM_BOT_CHAT_API

bot = telegram.Bot(api_token)
updater = Updater(token=api_token)
dispatcher: telegram.ext.dispatcher.Dispatcher = updater.dispatcher

updater.start_polling()

def send_message() -> None:
    """
    send messages by telegram bot
    """
    bot.sendMessage(chat_id=chat_id, text="3일 내 실적발표 기업들입니다.")
    for row in manufact_data.sort_close_earnings():
        bot.sendMessage(
            chat_id=chat_id,
            text=f"Ticker(종목코드): {row[0]} 종목명: {row[1]} 실적발표: {row[2]}"
            )
    bot.sendMessage(chat_id=chat_id, text="집중관찰하고 싶은 종목코드를 ,로 구분하여 작성해주세요.")
    manufact_data.append_input_totalrevenue()
# asyncio.run(send_message())

def echo(update: telegram.Update=None, context=None) -> List[str]:
    """
    user input at telegram bot
    다른 곳에서 호출할 때 telegram bot에서 필요한 update와 context 인자에 어떤 값을 써야할지 몰라서 기본값을 None으로 설정
    """
    user_text: List[str] = update.message.text.split(',')
    user_management = [element.replace(' ','').upper() for element in user_text]
    print(user_management)

    return user_management


send_message()

echo_handler: telegram.ext.messagehandler.MessageHandler = MessageHandler(Filters.text & ~Filters.command, echo)
dispatcher.add_handler(echo_handler)
