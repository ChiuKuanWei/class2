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
scores_df.sort_values(by='名次')

def fun1(series:pd.Series) -> int: 
    min = series.min()
    median = series.median()
    max = series.max()  
    s1 = pd.Series([min,median,max],index=["最低分","中間值","最高分"])
    return s1

subject_df = scores_df[['國文', '英文', '數學', '地理', '歷史']]

frame1 = subject_df.apply(fun1)
# print(frame1)

def fun2(series:pd.Series) -> pd.Series:
    lessThen60 = series[series<60].count()
    chinese = "及格" if(series['國文'] >= 60) else "不及格"
    english = "及格" if(series['英文'] >= 60) else "不及格"
    return pd.Series([lessThen60,chinese,english],index=['不及格科目',"國文","英文"])

def func3(series:pd.Series) -> int:
    return series[series<=60].count()

# def func4(series:pd.Series) -> str:
#     if(series[series< 70].count() > 0):
#         return 'Y'
#     else:
#         return 'N'
def func4(value:float)->str:
    return "禁假" if value < 70 else "不禁假"

# print(subject_df.T)
# print(subject_df.T.apply(fun2).T)

less60Count = scores_df[['國文', '英文', '數學', '地理', '歷史']].apply(func3,axis=1)
scores_df["不及格"] = less60Count
print(scores_df)

# scores_df["禁假"] = scores_df[['平均']].apply(func4,axis=1)
# print(scores_df)

scores_df["獎懲"] = scores_df['平均'].map(func4)
print(scores_df)

# print(scores_df.iloc[:3])
# new_df = scores_df.iloc[:3].copy()
# new_df["不及格"] = pd.Series([1,0,2],index=[1,2,3])
# print(new_df)

