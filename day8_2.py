import numpy as np
import pandas as pd

scores = np.random.randint(40, high=101, size=(50, 5))
scores_df = pd.DataFrame(scores,columns=['國文', '英文', '數學', '地理', '歷史'],index=range(1,51))
scores_df.index.name = "學號"
scores_df.columns.name="科目"
sum_series = scores_df.sum(axis=1)
mean_series = scores_df.mean(axis=1)
#display(sum_series)
rank_series = sum_series.rank(method='min',ascending=False)
scores_df["總分"] = sum_series
scores_df["平均"] = mean_series
scores_df["名次"] = rank_series
print(scores_df.sort_values(by='名次')) #依據'名次'列進行數值降序排序