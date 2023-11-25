import numpy as np
import pandas as pd

# array1 = np.array([1,2,3,4,5])
# print(array1)
# type(array1)

student_s= pd.Series({'姓名':'徐國堂','國文':78,'英文':89,'數學':79})
# print(student_s)
# print(student_s[1:] + 5)

S1 = pd.Series(np.arange(4.0,step=1))
# print(S1)
S1 = S1[-2:] *2
# print(S1)

# S2 = np.reshape(np.arange(16),(8,2))
# print(S2)

S2 = np.arange(16).reshape((4,4))
dataFrame = pd.DataFrame(S2,index=['台北','台中','高雄','台南'],columns=['one','two','three','four'])
print(dataFrame)
dataFrame2 = dataFrame.loc[['台北','台南']]  #loc[列，欄]
print(dataFrame2)

dataFrame3 = dataFrame.iloc[[0,1],[0,1,2]]  #iloc[列，欄]
print(dataFrame3)