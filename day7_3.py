import numpy as np
import pandas as pd

read_file = pd.read_csv('world.csv')
# print(read_file)

taiwan = read_file[read_file['國家'] == '台灣']
print(taiwan)

Japan = read_file[read_file['國家'] == '日本']
print(Japan)