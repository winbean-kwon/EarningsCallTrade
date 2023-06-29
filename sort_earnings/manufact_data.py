import requests
import csv
import config as config
import datetime


api_key = config.ALPHAVANTAGE_API_KEY
EARNINGS_CALENDAR_URL = 'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey={}'.format(api_key)

def get_earnings_calendar():
    with open('earnings_calendar.csv', 'w', encoding = "utf-8", newline='') as to_write:
        session = requests.Session()
        earnings_calendar = session.get(EARNINGS_CALENDAR_URL)
        decoded_content = earnings_calendar.content.decode('utf-8')
        my_list = list(csv.reader(decoded_content.splitlines(), delimiter=','))

        writer = csv.writer(to_write)
        writer.writerows(my_list)

    return my_list

def sort_close_earnings():
    sort_result = []
    current = datetime.date.today()

    with open('sort_earnings.csv', 'w', encoding = "utf-8", newline='') as to_write:
        writer = csv.writer(to_write)
        for row in get_earnings_calendar()[1:]:
            announce_date = datetime.datetime.strptime(row[2], '%Y-%m-%d').date()
            if (announce_date - current).days < 3 and row[4] != '':
                sort_result.append(row)
                writer.writerow(row)
                print(row)

    return sort_result

sort_close_earnings()


