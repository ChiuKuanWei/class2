import requests
import json
from fake_useragent import UserAgent

# 創建UserAgent物件
ua = UserAgent()
# 從UserAgent物件中獲取一個隨機的User-Agent，用於發送HTTP請求，降低被網站阻擋或限制的風險
user_agent = ua.random
my_head = {'user-agent': user_agent}

page_url = f'https://data.kcg.gov.tw/dataset/6f29f6f4-2549-4473-aa90-bf60d10895dc/resource/30dfc2cf-17b5-4a40-8bb7-c511ea166bd3/download/lightrailtraffic.json'

page_response = requests.get(page_url, headers= my_head)

page_content = page_response.content.decode(encoding='utf-8-sig')
# 將JSON轉換成Python字典
page_res_data = json.loads(page_content)
# print(page_res_data)
# 使用json.dumps()將字典轉換回JSON格式，indent參數指定縮排，ensure_ascii=False則允許輸出非ASCII字符，這樣中文字符就可以正確顯示
pretty_json = json.dumps(page_res_data, indent=2, ensure_ascii=False) 
print(pretty_json)
