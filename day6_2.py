import pandas as pd
import psycopg2
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://datatable1_user:JyUZ55hCqs2577TJsueAcutRdcD7oYPt@dpg-clc507mg1b2c73erocng-a.singapore-postgres.render.com/datatable1")
dataFrame = pd.read_sql_table("106人口密度",engine,columns=['統計年','區域別','年底人口數','土地面積','人口密度'])

# print(dataFrame[['區域別','年底人口數','土地面積']])

# for item in dataFrame['區域別']:
#     print(item)
    

# for item in dataFrame[['區域別','年底人口數','土地面積']]:
#     print(dataFrame[item])

for index,series in dataFrame[['區域別','土地面積','年底人口數']].iterrows():
    print(index, series['區域別'],series['土地面積'],series['年底人口數'])