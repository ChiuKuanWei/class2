import numpy as np
import pandas as pd

scroes = np.random.randint(50, 100,size=(50,5))
scores_df = pd.DataFrame(scroes,columns=['國文', '英文', '數學', '地理', '歷史'],index=range(1,51))
# print(scores_df)

scores_df['總分'] = scores_df.sum(axis = 1,skipna=True)
scores_df['平均'] = scores_df.mean(axis = 1,skipna=True)
print(scores_df)

# scores_df = scores_df.sort_values(by='總分',ascending=True).iloc[:5]
# print(scores_df)

#使用subscript[],過濾資料
scores_df1 = scores_df.query('平均<120 and 歷史<60')
print(scores_df1)



