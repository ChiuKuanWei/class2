import numpy as np
import pandas as pd

read_file = pd.read_csv('world.csv')
# print(read_file)

taiwan = read_file[read_file['國家'] == '台灣']
# print(taiwan)

Japan = read_file[read_file['國家'] == '日本']
# print(Japan)

# taiwan = read_file.query('日期>="2020-01-01" and 日期<="2020-01-31"')
# print(taiwan)

# 新增確診數最多的第一筆(Taiwan)
Max = taiwan.sort_values(by='新增確診數',ascending=False).iloc[:1]
print(Max)

Max2 = Japan.query('新增確診數>=50000')
print(Max2)