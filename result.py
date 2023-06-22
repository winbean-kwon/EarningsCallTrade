import requests
import csv
import config

api_key = config.alphavantage_api_key
CSV_URL = 'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey={}'.format(api_key)
url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=TSLA&apikey={}'.format(api_key)


r = requests.get(url)
data = r.json()

print(data)

with open('earnings_calendar.csv', 'w', encoding = "utf-8") as to_write:
    writer = csv.writer(to_write) 
    session = requests.Session()
    earnings_calendar = session.get(CSV_URL)

    decoded_content = earnings_calendar.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    
    for row in my_list:
        writer.writerow(row)
