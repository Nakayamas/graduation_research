#入水終了点および出水開始点の検出


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

csv='20171218/20171218_average_2_start_end.csv'

df = pd.read_csv(csv, header=None, names=['time', 'data'])
df_mean = df[500:-430]
mean = df_mean['data'].mean()

#df['data']=(df['data']*5)/1024
#mean=(mean*5)/1024

plt.plot(df['time'],df['data'],'#377eb8',label='data')
plt.axhline(mean, ls='-', c='#e41a1c', label='average')

plt.xlabel('Time [sec]')
#plt.ylabel('Voltage [V]')

plt.legend()
plt.show()


