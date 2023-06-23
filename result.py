import requests
import csv
import config
import datetime


current = datetime.date.today()
print(current)

api_key = config.alphavantage_api_key
CSV_URL = 'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey={}'.format(api_key)
url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=TSLA&apikey={}'.format(api_key)



with open('earnings_calendar.csv', 'w', encoding = "utf-8") as to_write:
    writer = csv.writer(to_write) 
    session = requests.Session()
    earnings_calendar = session.get(CSV_URL)

    decoded_content = earnings_calendar.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')

    my_list = list(cr)

# 3일 남은 종목들 솎아내서 텔레그램으로 전송하기 그럴라면 전체리스트에서 for문 돌려야할듯?
    result = []

    for row in my_list[1:]:
        announce_date = datetime.datetime.strptime(row[2], '%Y-%m-%d').date()
        
        if (announce_date - current).days < 3:
            result.append(row[1])
    
    print(result)

    
    for row in my_list:
        writer.writerow(row)
