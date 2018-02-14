#データのプロット


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


csv='20171218/20171218_average_2.csv'

df = pd.read_csv(csv, header=None, names=['time', 'data'])
#df['data']=(df['data']*5)/1024


plt.plot(df['time'],df['data'],'#377eb8',label='data')

plt.xlabel('Time [sec]')
plt.ylabel('Voltage [V]')

plt.legend()
plt.show()
