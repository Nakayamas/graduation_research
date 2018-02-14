#平均値フィルタをかける

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


load_csv='20171223/b/b_1.csv'
write_csv='20171223/b/b_1_ave.csv'
win=60

df = pd.read_csv(load_csv, header=None, names=['time', 'data'])
df_ave = pd.read_csv(load_csv, header=None, names=['time', 'data'])
df_ave['data'] = df_ave['data'].rolling(window=win, min_periods=10).mean()
df_ave=df_ave.rename(columns={'data':'ave'})

df_ave.to_csv(write_csv, index=False, header=None)

df['data']=(df['data']*5)/1024
df_ave['ave']=(df_ave['ave']*5)/1024

plt.plot(df['time'],df['data'],'b',label='raw_data')
plt.plot(df_ave['time'],df_ave['ave'],'r', label='avarage')

plt.xlabel('Time [sec]')
plt.ylabel('Sensor Output[V]')

plt.legend()
plt.show()
