# EarningsCallTrade

이 프로젝트는 미국 주식의 실적 발표 데이터를 자동으로 수집, 필터링하고, 텔레그램 봇을 통해 사용자에게 알림을 제공하며, 조건에 따라 자동 매매까지 수행할 수 있도록 하는 프로젝트입니다.

## 주요기능
- **실적 발표 데이터 수집**
    - Alpha Vantage API를 통해 3개월 이내의 Earnings Calendar 데이터를 수집합니다.
    - 위 데이터는 'earnings_calendar.csv' 파일로 저장됩니다.

- **필터링 및 정렬**
    - 발표일이 하루에서 이틀 이내이고, 총 매출이 일정 이상인 기업만 필터링 합니다.
    - 위 데이터는 'sort_earnings.csv'에 저장됩니다.

- **실적 발표 시간 크롤링**
    - Selenium을 이용해 [Earnings Whispers](https://www.earningswhispers.com/calendar)에서 발표 시간(BMO, AMC)을 크롤링합니다.
    - 수집된 시간은 장 이전, 이후 발표로 구분되어 'sort_earnings_tomorrow.csv'에 저장됩니다.

- **텔레그램 봇 알림**
    - 필터링된 종목을 텔레그램으로 전송하고, 사용자의 관심 종목 입력을 받아 응답합니다.

- **자동 매매 기능**
    - 한국투자증권 Open API ('mojito')를 통해 조건에 따라 종목을 시장가로 매수/매도할 수 있습니다. (증권 연결만 하고 실제 거래는 진행하지 않았습니다.)


---

## 설치 및 실행 방법

1. 의존성 설치:
    ```bash
    pip install -r requirements.txt
    ```

2. `config.py` 설정:
    ```python
    TELEGRAM_BOT_API = 'your-telegram-token'
    TELEGRAM_BOT_CHAT_API = 'your-chat-id'
    ALPHAVANTAGE_API_KEY = 'your-alpha-vantage-key'
    ```

3. 한국투자 API 키 파일 (`trading/koreainvestment.key`):
    ```
    <API_KEY>
    <SECRET_KEY>
    <ACCOUNT_NUMBER>
    ```

4. 실행:
    ```bash
    python earnings_sorting.py
    ```

---

## 텔레그램 봇 예시

