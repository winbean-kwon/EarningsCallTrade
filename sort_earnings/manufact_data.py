"""
This module provides functions for sorting earnings calendar data.
"""

import csv
import datetime
from typing import List
import requests
import config

import telegram_bot

api_key: str = config.ALPHAVANTAGE_API_KEY
EARNINGS_CALENDAR_URL: str = f'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey={api_key}'
session = requests.Session()

def get_earnings_calendar() -> List[List[str]]:
    """
    import earnings calendar to list
    """
    with open('earnings_calendar.csv', 'w', encoding = "utf-8", newline='') as to_write:
        earnings_calendar = session.get(EARNINGS_CALENDAR_URL)
        decoded_content: str = earnings_calendar.content.decode('utf-8')
        my_list: List[List[str]] = list(csv.reader(decoded_content.splitlines(), delimiter=','))

        writer = csv.writer(to_write)
        writer.writerows(my_list)

    return my_list

def sort_close_earnings() -> List[List[str]]:
    """
    sorts earning calendar to list
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

def append_input_totalrevenue() -> List[str]:
    """
    append totalrevenue from user input & close earnings
    """

    with open('sort_earnings.csv', 'r', encoding="utf-8") as to_read:
        reader = csv.reader(to_read)
        rows = list(reader)

    for row in rows:
        symbol = row[0]
        income_statement: str = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={api_key}'
        total_revenue = session.get(income_statement)
        row.append(total_revenue)

    with open('sort_earnings.csv','w', encoding = "utf-8", newline='') as to_write:
        writer = csv.writer(to_write)
        writer.writerows(rows)

# sort_close_earnings()

with open('sort_earnings.csv', 'r', encoding="utf-8") as to_read:
    reader = csv.reader(to_read)
    rows = list(reader)

for row in rows:
    symbol = row[0]
    income_statement: str = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={api_key}'
    total_revenue = session.get(income_statement)
    decoded_content: str = total_revenue.content.decode('utf-8')
    row.append(decoded_content)

    print(row)

# with open('sort_earnings.csv','w', encoding = "utf-8", newline='') as to_write:
#     writer = csv.writer(to_write)
#     writer.writerows(rows)





# api_key = config.alphavantage_api_key
# url = "https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=WBA&apikey={}".format(api_key)
# r = requests.get(url)
# data = r.json()
# for row in data["quarterlyReports"]:
#     ebitda = row["totalRevenue"]
#     print(ebitda)
