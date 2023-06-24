import requests
import csv
import config as config
import datetime


def get_earnings_calendar():
    api_key = config.alphavantage_api_key
    CSV_URL = 'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey={}'.format(api_key)
    url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=TSLA&apikey={}'.format(api_key)

    with open('earnings_calendar.csv', 'w', encoding = "utf-8") as to_write:
        session = requests.Session()
        earnings_calendar = session.get(CSV_URL)
        decoded_content = earnings_calendar.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')

        my_list = list(cr)

        for row in my_list:
            writer = csv.writer(to_write)
            writer.writerow(row)

    return my_list

def sort_close_earnings():
    my_list = get_earnings_calendar()
    result = []
    current = datetime.date.today()

    with open('sort_earnings.csv', 'w', encoding = "utf-8") as to_write:
        writer = csv.writer(to_write)
        for row in my_list[1:]:
            announce_date = datetime.datetime.strptime(row[2], '%Y-%m-%d').date()
            if (announce_date - current).days < 7:
                result.append(row)
                writer.writerow(row)

    return result

sort_close_earnings()