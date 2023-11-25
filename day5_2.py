import csv
import requests
import json
from fake_useragent import UserAgent
import certifi
import io
import pandas as pd

# file = open('個股日成交資訊.csv', mode='r', encoding='utf-8' , newline='')
# csv_reader = csv.reader(file)
# data_list = list(csv_reader)

# # 假设第一行包含标头
# headers = data_list[0]

# # 将数据转换为字典列表
# json_data = [dict(zip(headers, row)) for row in data_list[1:]]

# # 将字典列表转换为JSON格式的字符串
# json_string = json.dumps(json_data, indent=2, ensure_ascii=False)

# # 或者，您可以将JSON数据写入文件
# # with open('output.json', 'w', encoding='utf-8') as json_file:
# #     json.dump(json_data, json_file, ensure_ascii=False)

# print(json_string)

# 創建UserAgent物件
ua = UserAgent()
# 從UserAgent物件中獲取一個隨機的User-Agent，用於發送HTTP請求，降低被網站阻擋或限制的風險
user_agent = ua.random
my_head = {'user-agent': user_agent}

page_url = f'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv/file'
#page_url = f'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv/file'

page_response = requests.get(page_url, headers= my_head)
#page_content = page_response.content.decode(encoding='utf-8-sig')
#print(page_response.text)
file = io.StringIO(page_response.text)
csv_reader = csv.reader(file)
csv_list = list(csv_reader)
# for item in csv_list:
#     print(item)

df = pd.DataFrame(csv_list[1:],columns=csv_list[0])
df.to_csv("C://python-training//class2//106年度人口密度.csv")
print(df)



