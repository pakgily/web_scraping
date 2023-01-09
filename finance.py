import requests
import time
import datetime as dt
from bs4 import BeautifulSoup

codes = ['035420', '377300','009830','187660','068270'] # 종목코드 리스트
prices = [] # 가격정보가 담길 리스트

while True:
    prices = []
    for code in codes:
        time.sleep(10)
        url = 'https://finance.naver.com/item/main.nhn?code=' + code

        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        today = soup.select_one('#chart_area > div.rate_info > div')
        #today = soup.select_one('#chart_area > div.rate_info > div .blind')
        #today = soup.select_one('#chart_area > div.rate_info > div  span.blind')
        price = today.select_one('.blind')
        prices.append(price.get_text())
    prices.append(dt.datetime.now().strftime("%H, %M, %S"))
    print(prices)


a



