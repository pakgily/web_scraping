import requests
import pprint
import numpy as np
import pandas as pd
import dataframe_image as dfi
import collections, numpy

url = "https://finance.daum.net/api/charts/A005930/days?limit=200&adjusted=true"

headers = {
    "referer": "https://finance.daum.net/chart/A005930",
    "user-agent": "Mozilla/5.0"
}

params = {
    "limit": "100",
    "adjusted": "true"
}

resp = requests.get(url, headers=headers, params=params) #몇몇 웹사이트는 크롤러의 기계적인 접근을 막고 있음. 이를 우회하기 위해서 header 매개변수를 지정해주어야함.
data = resp.json()
#data1 = resp.text #UTF-8 인코딩 문자열

data = data['data']
data = pd.DataFrame(data)
print(data['date'])
# for day in data:
#     print(day['date'], day['tradePrice'])


writer = pd.ExcelWriter('C:/Users/hangilhangil3/Desktop/221220.xlsx', engine='xlsxwriter')
data.to_excel(writer,sheet_name='A')
writer.close()



    # def run(Analy):
    #     writer = pd.ExcelWriter('C:/Users/Administrator/Desktop/211102_기능안전.xlsx', engine='xlsxwriter')
    #     sheet_name = ['env', 'SG1', 'SG3', 'SG4', 'SG5', 'GenSF']
    #     i = 0
    #     while i < len(Analy):
    #         j = 0
    #         start_row = 1
    #         Analy_shape = [start_row]
    #         while j < len(Analy[i]):
    #             if len(Analy[i][j]) != 0:  # Gear Ref.와 같이 일반적인 주행 데이터로는 데이터 취득이 되지 않은 경우를 위하여 Skip을 위해
    #                 Analy[i][j].to_excel(writer, sheet_name=sheet_name[i], startrow=start_row, startcol=0)
    #                 Analy_shape.append(Analy[i][j].shape[0] + 3)
    #                 start_row = np.array(Analy_shape).sum()
    #             j += 1
    #         i += 1
    #     writer.close()
