import numpy as np
import pandas as pd
from openpyxl import load_workbook

scroes = np.random.randint(50, 100,size=(50,5))
scores_df = pd.DataFrame(scroes,columns=['國文', '英文', '數學', '地理', '歷史'],index=range(1,51))
# print(scores_df)

scores_df['總分'] = scores_df.sum(axis = 1,skipna=True)
scores_df['平均'] = scores_df.mean(axis = 1,skipna=True)
# print(scores_df)

scores_df.style\
    .format(precision=2)\
    .highlight_between(left=50,right=59,props='color:white; background-color:#CB1B45;')\
    .highlight_max(axis=1,subset=scores_df.columns[:5],props='color:white; background-color:#2B5F75;')

book = load_workbook('天龍國小.xlsx')


# scores_df = scores_df.sort_values(by='總分',ascending=True).iloc[:5]
# print(scores_df)

#使用subscript[],過濾資料
# scores_df1 = scores_df.query('平均<120 and 歷史<60')
# print(scores_df1)



