from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8')
# pprint(html.text)

soup = bs(html.text,'html.parser')

#data1 = soup.find('li',{'class':'item_today level1'}).text
data1 = soup.findAll('ul',{'class':'today_chart_list'})

list = []
for t in data1:
    list.append(t.text)

print(list)

title = soup.select_one('#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.weather_graphic > div.temperature_text > strong')
print(title.get_text())