import numpy as np
import pandas as pd
import requests

#每日進站人口數,政府開放平台 - https://data.gov.tw/dataset/8792
url1 = 'https://ods.railway.gov.tw/tra-ods-web/ods/download/dataResource/8ae4cabf6973990e0169947ed32454b9'

#車站基本資料集 - https://data.gov.tw/dataset/33425
url2 = 'https://ods.railway.gov.tw/tra-ods-web/ods/download/dataResource/0518b833e8964d53bfea3f7691aea0ee'

response = requests.get(url1)
sites = response.json()
# print(sites)
response = requests.get(url2)
site_info = response.json()
# print(site_info)
site_entry_df = pd.DataFrame(sites)
site_entry_df.columns = ['乘車日','車站代碼','進站人數','出站人數']
# print(site_entry_df)
site_info_df = pd.DataFrame(site_info,columns=["stationCode","stationName"])
site_info_df.columns = ["車站代碼","中文站名"]
# print(site_info_df)

sites_df = pd.merge(site_entry_df,site_info_df,how="left",left_on="車站代碼",right_on="車站代碼")
sites_df1 = sites_df.reindex(columns=["乘車日","中文站名","進站人數","出站人數"])
print(sites_df1)

eight = sites_df1.query('中文站名=="八堵"')
print(eight)

seven = sites_df1.query('中文站名=="七堵"')
print(seven)

pd.concat([eight,seven])