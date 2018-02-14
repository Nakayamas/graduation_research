#水圧センサデータとその乖離率をプロット



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


csv = '20171218/20171218_average_2.csv'
win_kairi = 35


df_start = pd.read_csv(csv, header=None, names=['time', 'data'])
df_start['ave'] = df_start['data'].rolling(window=win_kairi).mean()
df_start['kairi'] = (df_start['data'] - df_start['ave'])/df_start['ave'] * 100

df_start_kairi=df_start.query('kairi >= 0.31').loc[:,['time','data','ave','kairi']]


df_end = pd.read_csv(csv, header=None, names=['time', 'data'])
df_end=df_end[::-1]
df_end['ave']=df_end['data'].rolling(window=win_kairi).mean()
df_end=df_end[::-1]
df_end['kairi'] = (df_end['data'] - df_end['ave'])/df_end['ave'] * 100

df_end_kairi=df_end.query('kairi >= 0.33').loc[:,['time','data','ave','kairi']]

print('-------start------')
print(df_start_kairi)

kairi_st = 0.31
kairi_end = 0.33

#df_start['data']=(df_start['data']*5)/1024

plt.subplot(212)
plt.xlabel('Time [sec]')
#plt.ylabel('Voltage [V]')
plt.plot(df_start['time'],df_start['data'],'#377eb8')

plt.subplot(211)
plt.ylabel('Rate of divergence [%]')
plt.plot(df_start['time'],df_start['kairi'],'#4daf4a')
plt.axhline(kairi_st, ls='-', c='#e41a1c')
plt.axhline(0, ls='-', c='darkgrey')

plt.show()

print('------end------')
print(df_end_kairi)


#df_end['data']=(df_end['data']*5)/1024

plt.subplot(212)
plt.xlabel('Time [sec]')
#plt.ylabel('Voltage [V]')
plt.plot(df_end['time'],df_end['data'],'#377eb8')

plt.subplot(211)
plt.ylabel('Rate of divergence [%]')
plt.plot(df_end['time'],df_end['kairi'],'#4daf4a')
plt.axhline(kairi_end, ls='-', c='#e41a1c')
plt.axhline(0, ls='-', c='darkgrey')

plt.show()


