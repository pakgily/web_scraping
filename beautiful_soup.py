import requests
from bs4 import BeautifulSoup

url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt > a')
    print(title.get_text())

else :
    print(response.status_code)


    # footer > div > div.aside_area > div.partner_box_wrap > div:nth-child(1) > a:nth-child(3)