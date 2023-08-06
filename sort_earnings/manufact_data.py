"""
This module provides functions for sorting earnings calendar data.
"""

import csv
import datetime
from typing import List
import requests
import config
import time
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from trading import crawling
import telegram_bot


api_key: str = config.ALPHAVANTAGE_API_KEY
EARNINGS_CALENDAR_URL: str = f'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey=""'
session = requests.Session()

# def get_earnings_calendar() -> List[List[str]]:
#     """
#     import earnings calendar to list
#     """
#     with open('earnings_calendar.csv', 'w', encoding = "utf-8", newline='') as to_write:
#         earnings_calendar = session.get(EARNINGS_CALENDAR_URL)
#         decoded_content: str = earnings_calendar.content.decode('utf-8')
#         my_list: List[List[str]] = list(csv.reader(decoded_content.splitlines(), delimiter=','))

#         writer = csv.writer(to_write)
#         writer.writerows(my_list)

#     return my_list

# def sort_close_earnings() -> List[List[str]]:
#     """
#     sorts earning calendar to list
#     """
#     sort_result: List[List[str]] = []
#     current = datetime.date.today()

#     count = 1

#     with open('sort_earnings.csv', 'w', encoding = "utf-8", newline='') as to_write:
#         writer = csv.writer(to_write)
#         for row in get_earnings_calendar()[1:]:
#             announce_date = datetime.datetime.strptime(row[2], '%Y-%m-%d').date()
#             try:
#                 if (announce_date - current).days < 3 and row[4] != '':
#                     symbol = row[0]
#                     print(symbol)
#                     get_income_statement: str = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey=""'
#                     response = requests.get(get_income_statement)
#                     print(response)
#                     income_statement = response.json()
#                     time.sleep(5)
#                     if "quarterlyReports" in income_statement and int(income_statement["quarterlyReports"][0]["totalRevenue"]) > 10000000:
#                         recent_total_revenue = income_statement["quarterlyReports"][0]["totalRevenue"]
#                         row.append(recent_total_revenue)
#                         sort_result.append(row)
#                         writer.writerow(row)
#                         print(count)
#                         count += 1
            
#                 if count >= 5: # 1분에 api 5번 요청 가능하고, 하루에 100번밖에 안됨.
#                     time.sleep(60)
#                     count = 0
            
#             except Exception as e:
#                 print(f"An error occurred for report at index {row[0]}: {e}")
#                 continue

#     return sort_result

def compare():
    with open('sort_earnings.csv', 'r', encoding = "utf-8", newline='') as csv_file:
        reader = csv.reader(csv_file)
        print(crawling.before_total_crawle)
        with open('sort_earnings.csv', 'a', encoding = "utf-8", newline='') as csv_file:
            writer = csv.writer(csv_file)
            for row in reader:
                for key, value in crawling.before_total_crawle.items():
                    if row[0] == key:
                        row.append(value)
                        writer.writerow(row)

                for key, value in crawling.after_total_crawle.items():
                    if row[0] == key:
                        row.append(value)
                        writer.writerow(row)
            

compare()
        


# Q. 2번 파일에서 1번 파일을 호출한 후, 1번 파일에서 2번 파일을 다시 호출해도되나?

# totalrevenue 데이터 긁어와서 sort_earnings에 추가하는 로직 만들기
# BMO(Before Market 종목들 크롤링 AMO는 investing.com에서 크롤링해도 될듯?)
# api_key = config.alphavantage_api_key
# url = "https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=WBA&apikey={}".format(api_key)
# r = requests.get(url)
# data = r.json()
# for row in data["quarterlyReports"]:
#     ebitda = row["totalRevenue"]
#     print(ebitda)
