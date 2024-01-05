#Fourier - Grupo 33

from lab import *

T = 0.4  # Período
T1 = 0.2 # 
T2 = 0.1 #
t = timevar(20)
t1 = 0.2
t2 = 0.35
a0 = 2.125
w0 = 2 * pi / T  # Frequência fundamental
N = 10  # Número de harmônicas
x = a0

for k in range(1, N + 1):
    coef1 = (15 * sin(k * pi * T1 / T) / (k * pi)) * exp(-1j * k * w0 * t1)
    coef2 = (-30 * sin(k * pi * T2 / T) / (k * pi)) * exp(-1j * k * w0 * t2)
    bk = coef1 + coef2
    ak = bk / (1j * w0 * k)

    if k == 3:
        print("B_k", k, "=", bk)
        print("A_k", k, "=", ak)

    coef1_neg = (15 * sin(-k * pi * T1 / T) / (-k * pi)) * exp(-1j * -k * w0 * t1)
    coef2_neg = (-30 * sin(-k * pi * T2 / T) / (-k * pi)) * exp(-1j * -k * w0 * t2)
    b_k = coef1_neg + coef2_neg
    a_k = b_k / (1j * w0 * -k)

    if k == 1:
        print("B_-k", k, "=", b_k)
        print("A_-k", k, "=", a_k)

    x = x + ak * exp(k * w0 * t * 1j) + a_k * exp(-k * w0 * t * 1j)
    tplot(x)
