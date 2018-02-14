#開始時間を0スタート


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

csv_st='20171223/a/a_1_start.csv'
csv_end = '20171223/a/a_1_end.csv'


zero_st = pd.read_csv(csv_st, header=None, names=['time', 'data'])
zero_st['time'] = zero_st['time'] - zero_st.ix[0,0]
zero_st.to_csv(csv_st, index=False, header=None)

zero_end = pd.read_csv(csv_end, header=None, names=['time', 'data'])
zero_end['time'] = zero_end['time'] - zero_end.ix[0,0]
zero_end.to_csv(csv_end, index=False, header=None)


print('-------start------')
print(zero_st)

print('------end------')
print(zero_end)
