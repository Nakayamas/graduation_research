#各データとの水位変化量の差を算出


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

write_csv = 'unk_vari_d5.csv'
load_csv = 'vari.csv'
x = 19


vari = pd.read_csv(load_csv, header=None, names=['time', 'data'])

df = pd.DataFrame([], columns = ['distance'])

for i in range(20):
    df2 = pd.DataFrame([math.fabs(vari.ix[x,1] - vari.ix[i,1])], columns=['distance'], index = [i])
    df = df.append(df2)


print(df)
df.to_csv(write_csv, index=False, header=None)
