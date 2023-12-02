import numpy as np
import pandas as pd

frame = pd.DataFrame(np.random.randn(4,3),
             columns=['d','f','e'],
             index=['台北','台中','台南','高雄']
            )
print(np.absolute(frame))

#使用for in 讀取DataFrame
for column in frame:
    for item in frame[column]:
        print(item)
    print("=======")

#使用for in 讀取DataFrame
for column in frame:
    print(np.abs(frame[column]))