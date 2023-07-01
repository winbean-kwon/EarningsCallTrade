"""
This module provides functions for sorting earnings calendar data.
"""

import csv
import datetime
from typing import List
import requests
import config


api_key: str = config.ALPHAVANTAGE_API_KEY
EARNINGS_CALENDAR_URL: str = f'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey={api_key}'


def get_earnings_calendar() -> List[List[str]]:
    """
    This function import earnings calendar to list
    """
    with open('earnings_calendar.csv', 'w', encoding = "utf-8", newline='') as to_write:
        session = requests.Session()
        earnings_calendar = session.get(EARNINGS_CALENDAR_URL)
        decoded_content: str = earnings_calendar.content.decode('utf-8')
        my_list: List[List[str]] = list(csv.reader(decoded_content.splitlines(), delimiter=','))

        writer = csv.writer(to_write)
        writer.writerows(my_list)

    return my_list

def sort_close_earnings() -> List[List[str]]:
    """
    This function sorts earning calendar to list
    """
    sort_result: List[List[str]] = []
    current = datetime.date.today()

    with open('sort_earnings.csv', 'w', encoding = "utf-8", newline='') as to_write:
        writer = csv.writer(to_write)
        for row in get_earnings_calendar()[1:]:
            announce_date = datetime.datetime.strptime(row[2], '%Y-%m-%d').date()
            if (announce_date - current).days < 3 and row[4] != '':
                sort_result.append(row)
                writer.writerow(row)

    return sort_result

sort_close_earnings()


# sort_close_earnings()

# totalrevenue 데이터 긁어와서 sort_earnings에 추가하는 로직 만들기
# url에 2개의 변수가 있으면 어떻게 호출해야하는지?
# 어떤 함수에서 호출해서 사용해야할지? api_key를 함수 바깥에 두면 나중에 다른 곳에서 호출할 때 지장이 없을지?
# api_key = config.alphavantage_api_key
# url = "https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=WBA&apikey={}".format(api_key)
# r = requests.get(url)
# data = r.json()
# for row in data["quarterlyReports"]:
#     ebitda = row["totalRevenue"]
#     print(ebitda)
