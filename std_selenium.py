'''
Selenium 스터디
 : 동적페이지 중, 데이터를 따로 받아서 완성시키는 페이지는
 Beautiful soup으로 가져오는 경우에 실패하는 경우가 있음.
 따라서 이 때 selenium을 활용하면 쉽게 해결 가능함.
'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/ssamko/Downloads/chromedriver")
url = "https://weather.naver.com/today/02135108"
driver.get(url)

result = requests.get(url)

bs_obj1 = BeautifulSoup(url, "html.parser")
bs_obj2 = BeautifulSoup(driver.page_source, "html.parser")


'''
1. Select(), select_one() 매개변수
  - 태그이름
  - .클래스이름
  - #아이디이름
  - 상위태그이름 > 자식태그 > 자식태그
  - 상위태그이름 자손태그 
      :자식을 건너 띈다
  - [속성]
  - 태그이름.클래스이름
  - #아이디이름 > 태그이름.클래스이름
      : 아이디이름으로 찾고 자식태크와 클래스이름으로 찾음
'''
current_humidity = bs_obj1.select_one("#now > div > div.weather_area > div.weather_quick_area > div > div.scroll_area > div > div.weather_quick._cnCrntWeatherSummary > div > ul:nth-child(1) > li:nth-child(1) > dl")
print(current_humidity)

current_humidity = bs_obj2.select_one("#now > div > div.weather_area > div.weather_quick_area > div > div.scroll_area > div > div.weather_quick._cnCrntWeatherSummary > div > ul:nth-child(1) > li:nth-child(1) > dl")
print(current_humidity.text)

#now > div > div.weather_area > div.weather_quick_area > div > div.scroll_area > div > div.weather_quick._cnCrntWeatherSummary > div > ul:nth-child(1) > li:nth-child(1) > dl > dd > em