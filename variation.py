#各データの水位変化量を算出

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

write_csv = 'vari.csv'

csv_a1='20171223/a/a_1_ave.csv'
csv_a2='20171223/a/a_2_ave.csv'
csv_a3='20171223/a/a_3_ave.csv'
csv_a4='20171223/a/a_4_ave.csv'
csv_a5='20171223/a/a_5_ave.csv'
csv_b1='20171223/b/b_1_ave.csv'
csv_b2='20171223/b/b_2_ave.csv'
csv_b3='20171223/b/b_3_ave.csv'
csv_b4='20171223/b/b_4_ave.csv'
csv_b5='20171223/b/b_5_ave.csv'
csv_c1='20171223/c/c_1_ave.csv'
csv_c2='20171223/c/c_2_ave.csv'
csv_c3='20171223/c/c_3_ave.csv'
csv_c4='20171223/c/c_4_ave.csv'
csv_c5='20171223/c/c_5_ave.csv'
csv_d1='20171223/d/d_1_ave.csv'
csv_d2='20171223/d/d_2_ave.csv'
csv_d3='20171223/d/d_3_ave.csv'
csv_d4='20171223/d/d_4_ave.csv'
csv_d5='20171223/d/d_5_ave.csv'


def var(csv_name):
    df_var = pd.read_csv(csv_name, header=None, names=['time', 'data'])
    df_st = df_var[:250]
    st = df_st['data'].mean()

    df_mean = df_var[500:-430]
    mean = df_mean['data'].mean()

    variation = mean - st
    return variation

df = pd.DataFrame({'name':["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5"]})

df['variation'] = [var(csv_a1),
                    var(csv_a2),
                    var(csv_a3),
                    var(csv_a4),
                    var(csv_a5),
                    var(csv_b1),
                    var(csv_b2),
                    var(csv_b3),
                    var(csv_b4),
                    var(csv_b5),
                    var(csv_c1),
                    var(csv_c2),
                    var(csv_c3),
                    var(csv_c4),
                    var(csv_c5),
                    var(csv_d1),
                    var(csv_d2),
                    var(csv_d3),
                    var(csv_d4),
                    var(csv_d5)]


df.to_csv(write_csv, index=False, header=None)

print(df)
