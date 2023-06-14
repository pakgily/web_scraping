'''
BeautifulSoup 스터디
1. Select, Select_one
'''

import requests
from bs4 import BeautifulSoup

url = "https://weather.naver.com/today/02135108"

result = requests.get(url)

bs_obj = BeautifulSoup(result.content, "html.parser")

location = bs_obj.findAll("strong",{"class":"location_name"})
print(location[0].text)


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
current_area = bs_obj.select_one("div.location_area > strong.location_name")
print(current_area.text)

current_temp = bs_obj.select_one("div.weather_area .current")
print(current_temp.text.replace("현재 온도",""))

current_humidity = bs_obj.select_one("div.weather_quick_area")
print(current_humidity)