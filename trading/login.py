import mojito

def login_stock():
    file = open("trading/koreainvestment.key")
    lines = file.readlines()
    key = lines[0].strip()
    secret_key = lines[1].strip()
    account_number = lines[2].strip()
    file.close()

    broker = mojito.KoreaInvestment(
        api_key = key,
        api_secret = secret_key,
        acc_no = account_number,
        exchange = '나스닥'
    )

    print(broker)

    return broker

login_stock()