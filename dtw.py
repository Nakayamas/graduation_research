#dtw距離を算出


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

write_csv = 'dtw_result/d5.csv'

csv1_st = '20171223/a/a_1_start.csv'
csv1_end = '20171223/a/a_1_end.csv'

csv2_st = '20171223/a/a_2_start.csv'
csv2_end = '20171223/a/a_2_end.csv'

csv3_st = '20171223/a/a_3_start.csv'
csv3_end = '20171223/a/a_3_end.csv'

csv4_st = '20171223/a/a_4_start.csv'
csv4_end = '20171223/a/a_4_end.csv'

csv5_st = '20171223/a/a_5_start.csv'
csv5_end = '20171223/a/a_5_end.csv'

csv6_st = '20171223/b/b_1_start.csv'
csv6_end = '20171223/b/b_1_end.csv'

csv7_st = '20171223/b/b_2_start.csv'
csv7_end = '20171223/b/b_2_end.csv'

csv8_st = '20171223/b/b_3_start.csv'
csv8_end = '20171223/b/b_3_end.csv'

csv9_st = '20171223/b/b_4_start.csv'
csv9_end = '20171223/b/b_4_end.csv'

csv10_st = '20171223/b/b_5_start.csv'
csv10_end = '20171223/b/b_5_end.csv'

csv11_st = '20171223/c/c_1_start.csv'
csv11_end = '20171223/c/c_1_end.csv'

csv12_st = '20171223/c/c_2_start.csv'
csv12_end = '20171223/c/c_2_end.csv'

csv13_st = '20171223/c/c_3_start.csv'
csv13_end = '20171223/c/c_3_end.csv'

csv14_st = '20171223/c/c_4_start.csv'
csv14_end = '20171223/c/c_4_end.csv'

csv15_st = '20171223/c/c_5_start.csv'
csv15_end = '20171223/c/c_5_end.csv'

csv16_st = '20171223/d/d_1_start.csv'
csv16_end = '20171223/d/d_1_end.csv'

csv17_st = '20171223/d/d_2_start.csv'
csv17_end = '20171223/d/d_2_end.csv'

csv18_st = '20171223/d/d_3_start.csv'
csv18_end = '20171223/d/d_3_end.csv'

csv19_st = '20171223/d/d_4_start.csv'
csv19_end = '20171223/d/d_4_end.csv'

csv20_st = '20171223/d/d_5_start.csv'
csv20_end = '20171223/d/d_5_end.csv'

a1_st = pd.read_csv(csv1_st, header=None, names=['time', 'data'])
a1_end = pd.read_csv(csv1_end, header=None, names=['time', 'data'])

a2_st = pd.read_csv(csv2_st, header=None, names=['time', 'data'])
a2_end = pd.read_csv(csv2_end, header=None, names=['time', 'data'])

a3_st = pd.read_csv(csv3_st, header=None, names=['time', 'data'])
a3_end = pd.read_csv(csv3_end, header=None, names=['time', 'data'])

a4_st = pd.read_csv(csv4_st, header=None, names=['time', 'data'])
a4_end = pd.read_csv(csv4_end, header=None, names=['time', 'data'])

a5_st = pd.read_csv(csv5_st, header=None, names=['time', 'data'])
a5_end = pd.read_csv(csv5_end, header=None, names=['time', 'data'])

b1_st = pd.read_csv(csv6_st, header=None, names=['time', 'data'])
b1_end = pd.read_csv(csv6_end, header=None, names=['time', 'data'])

b2_st = pd.read_csv(csv7_st, header=None, names=['time', 'data'])
b2_end = pd.read_csv(csv7_end, header=None, names=['time', 'data'])

b3_st = pd.read_csv(csv8_st, header=None, names=['time', 'data'])
b3_end = pd.read_csv(csv8_end, header=None, names=['time', 'data'])

b4_st = pd.read_csv(csv9_st, header=None, names=['time', 'data'])
b4_end = pd.read_csv(csv9_end, header=None, names=['time', 'data'])

b5_st = pd.read_csv(csv10_st, header=None, names=['time', 'data'])
b5_end = pd.read_csv(csv10_end, header=None, names=['time', 'data'])

c1_st = pd.read_csv(csv11_st, header=None, names=['time', 'data'])
c1_end = pd.read_csv(csv11_end, header=None, names=['time', 'data'])

c2_st = pd.read_csv(csv12_st, header=None, names=['time', 'data'])
c2_end = pd.read_csv(csv12_end, header=None, names=['time', 'data'])

c3_st = pd.read_csv(csv13_st, header=None, names=['time', 'data'])
c3_end = pd.read_csv(csv13_end, header=None, names=['time', 'data'])

c4_st = pd.read_csv(csv14_st, header=None, names=['time', 'data'])
c4_end = pd.read_csv(csv14_end, header=None, names=['time', 'data'])

c5_st = pd.read_csv(csv15_st, header=None, names=['time', 'data'])
c5_end = pd.read_csv(csv15_end, header=None, names=['time', 'data'])

d1_st = pd.read_csv(csv16_st, header=None, names=['time', 'data'])
d1_end = pd.read_csv(csv16_end, header=None, names=['time', 'data'])

d2_st = pd.read_csv(csv17_st, header=None, names=['time', 'data'])
d2_end = pd.read_csv(csv17_end, header=None, names=['time', 'data'])

d3_st = pd.read_csv(csv18_st, header=None, names=['time', 'data'])
d3_end = pd.read_csv(csv18_end, header=None, names=['time', 'data'])

d4_st = pd.read_csv(csv19_st, header=None, names=['time', 'data'])
d4_end = pd.read_csv(csv19_end, header=None, names=['time', 'data'])

d5_st = pd.read_csv(csv20_st, header=None, names=['time', 'data'])
d5_end = pd.read_csv(csv20_end, header=None, names=['time', 'data'])


def dtw(vec1, vec2):
    d = np.zeros([len(vec1)+1, len(vec2)+1])
    d[:] = np.inf
    d[0, 0] = 0
    for i in range(1, d.shape[0]):
        for j in range(1, d.shape[1]):
            cost = abs(vec1[i-1]-vec2[j-1])
            d[i, j] = cost + min(d[i-1, j], d[i, j-1], d[i-1, j-1])
    return d[-1][-1]


unk_st = d5_st['data']
unk_end = d5_end['data']


dataframe = pd.DataFrame({'name':["A1","A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5"]})

dataframe['start'] = [dtw(unk_st,a1_st['data']),
                        dtw(unk_st,a2_st['data']),
                        dtw(unk_st,a3_st['data']),
                        dtw(unk_st,a4_st['data']),
                        dtw(unk_st,a5_st['data']),
                        dtw(unk_st,b1_st['data']),
                        dtw(unk_st,b2_st['data']),
                        dtw(unk_st,b3_st['data']),
                        dtw(unk_st,b4_st['data']),
                        dtw(unk_st,b5_st['data']),
                        dtw(unk_st,c1_st['data']),
                        dtw(unk_st,c2_st['data']),
                        dtw(unk_st,c3_st['data']),
                        dtw(unk_st,c4_st['data']),
                        dtw(unk_st,c5_st['data']),
                        dtw(unk_st,d1_st['data']),
                        dtw(unk_st,d2_st['data']),
                        dtw(unk_st,d3_st['data']),
                        dtw(unk_st,d4_st['data']),
                        dtw(unk_st,d5_st['data'])]

dataframe['end'] = [dtw(unk_end,a1_end['data']),
                        dtw(unk_end,a2_end['data']),
                        dtw(unk_end,a3_end['data']),
                        dtw(unk_end,a4_end['data']),
                        dtw(unk_end,a5_end['data']),
                        dtw(unk_end,b1_end['data']),
                        dtw(unk_end,b2_end['data']),
                        dtw(unk_end,b3_end['data']),
                        dtw(unk_end,b4_end['data']),
                        dtw(unk_end,b5_end['data']),
                        dtw(unk_end,c1_end['data']),
                        dtw(unk_end,c2_end['data']),
                        dtw(unk_end,c3_end['data']),
                        dtw(unk_end,c4_end['data']),
                        dtw(unk_end,c5_end['data']),
                        dtw(unk_end,d1_end['data']),
                        dtw(unk_end,d2_end['data']),
                        dtw(unk_end,d3_end['data']),
                        dtw(unk_end,d4_end['data']),
                        dtw(unk_end,d5_end['data'])]

dataframe['total'] = dataframe['start'] + dataframe['end']

print(dataframe)

dataframe.to_csv(write_csv, index=False, header=None)

