import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

# 時系列のサンプルデータ作成
n = 512                         # データ数
dt = 0.01                       # サンプリング間隔
f = 1                           # 周波数
t = np.linspace(1, n, n)*dt-dt
y = np.sin(2*np.pi*f*t)+0.5*np.random.randn(t.size)
n2 = n//2


# FFT 処理と周波数スケールの作成
yf = fftpack.fft(y)/(n/2)
freq = fftpack.fftfreq(n, dt)

# フィルタ処理
# ここではカットオフ周波数以上に対応するデータを 0 にしている
fs = 2                          # カットオフ周波数[Hz]
yf2 = np.copy(yf)
yf2[(freq > fs)] = 0
yf2[(freq < 0)] = 0

# 逆 FFT 処理
# FFT によるフィルタ処理では虚数部が計算されることがあるため
# real 関数が必要(普段は必要ない)
y2 = np.real(fftpack.ifft(yf2)*n)

# rfft 関数を使う場合には yf, y2 は以下のように求まる
# rfft はナイキスト周波数以上の帯域を計算しないため負荷が軽い
# yf = fftpack.rfft(y)//(n/2)
# y2 = fftpack.irfft(yf2)*(n/2)

# プロット
plt.figure(1)
plt.subplot(211)
plt.plot(freq[1:n2], np.abs(yf[1:n2]))
plt.ylabel("Amplitude")
plt.axis("tight")
plt.subplot(212)
plt.plot(freq[1:n2], np.abs(yf2[1:n2]))
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.axis("tight")

plt.figure(2)
plt.plot(t, y, "b", label="original")
plt.plot(t, y2, "r", linewidth=2, label="filtered")
plt.axis("tight")
plt.legend(loc="upper right")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
