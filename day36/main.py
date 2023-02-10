import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "API_KEY"
STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_API = "API_KEY"
check_increased = False
account_ssid = "Account_SID"
account_auth = "ACCOUNT_AUTH"
increased_icon ="🔺"
decreased_icon ="🔻"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def check_stock():
    parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "datatype": "json",
        "outputsize": "compact",
        "apikey": STOCK_API
    }
    global check_increased
    response = requests.get(url=STOCK_URL, params=parameters)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    yesterday_data = data_list[0]
    yesterday_closing = float(yesterday_data['4. close'])
    day_before_data = data_list[1]
    day_before_closing = float(day_before_data['4. close'])
    five_val = (day_before_closing / 100) * 5
    if day_before_closing - five_val > yesterday_closing:
        get_news()
    elif yesterday_closing > day_before_closing + five_val:
        check_increased = True
        get_news()


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    parameters = {
        "q": COMPANY_NAME,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": NEWS_API
    }
    response = requests.get(url=NEWS_URL, params=parameters)
    response.raise_for_status()
    data = response.json()['articles']
    news_list = []
    for i in range(0, 3):
        new_dict = {
            "title": data[i]['title'],
            "body": data[i]['description']
        }
        news_list.append(new_dict)
    send_news(news_list)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_news(news_list):
    global check_increased
    client = Client(account_ssid, account_auth)
    if check_increased:
        message = client.messages.create(
            body=f"{STOCK}: {increased_icon}5% \nHeadline: {news_list[0]['title']} \nBrief: {news_list[0]['body']}",
            from_='sender mobileno.',
            to='mobileno. receiver'
        )
    else:
        message = client.messages.create(
            body=f"{STOCK}: {decreased_icon}5% \nHeadline: {news_list[0]['title']} \nBrief: {news_list[0]['body']}",
            from_='sender mobileno.',
            to='mobileno. receiver'
        )
    print(message.sid)




# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
check_stock()

