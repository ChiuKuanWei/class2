#建立postgresql資料庫

import pandas as pd 
import psycopg2
from sqlalchemy import create_engine

url = 'https://raw.githubusercontent.com/roberthsu2003/PythonForDataAnalysis/master/pandas%E7%9A%84%E6%AA%94%E6%A1%88%E5%AD%98%E5%8F%96/%E5%90%84%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80%E4%BA%BA%E5%8F%A3%E5%AF%86%E5%BA%A6.csv'
dataFrame = pd.read_csv(url)
# print(dataFrame)

dataFrame.columns = dataFrame.iloc[0]
dataFrame1=dataFrame.drop(index=0)
dataFrame2=dataFrame1.drop(index=[371,372,373,374,375])
# print(dataFrame2)

#連線位置(postgres://datatable1_user:JyUZ55hCqs2577TJsueAcutRdcD7oYPt@dpg-clc507mg1b2c73erocng-a.singapore-postgres.render.com/datatable1)
engine = create_engine("postgresql+psycopg2://datatable1_user:JyUZ55hCqs2577TJsueAcutRdcD7oYPt@dpg-clc507mg1b2c73erocng-a.singapore-postgres.render.com/datatable1")
# dataFrame2.to_sql("106人口密度",engine,if_exists='replace')
dataFrame3 = pd.read_sql_table("106人口密度",engine,columns=['統計年','區域別','年底人口數','土地面積','人口密度'])
print(dataFrame3)