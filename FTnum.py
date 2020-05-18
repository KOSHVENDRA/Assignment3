# Computing fourier transform (FT) of sinc function using numpy
# Author : Koshvendra Singh
# Email  : koshvendra1999@gmail.com
# Date   : 09/05/2020

import numpy as np
import matplotlib.pyplot as plt

# sinc = sin(x*pi)/x*pi  in numpy

xmax=50
xmin=-50

N=256                                    # no. of sampling points 
dx=(xmax-xmin)/(N-1)                     # resolution

sampled_data= []
xarr=[]

for i in range(N):
    sampled_data.append(np.sinc((xmin + i*dx)/np.pi))
    xarr.append(xmin + i*dx)

sinc_fft=np.fft.fft(sampled_data,norm="ortho")    # FT of sinc function

freq=np.fft.fftfreq(N,dx)                  # frequency array
freq=2*np.pi*freq
factor=np.exp(-1j*freq*xmin)
freq_s=np.fft.fftshift(freq)               # shifted frequency array

ft=dx*np.sqrt(N/(2*np.pi))*factor*sinc_fft   # multiplying the factors to FT
ft_s=np.fft.fftshift(ft)                  # shifted FT

# definig the exact FT of sinc function
def ext_sinc(x):
    if np.absolute(x)<=1:
        return ((np.pi/2)**0.5)
    else:
        return (0)

ext_sinc_arr=[]
for i in range(len(freq_s)):
    k=ext_sinc(freq_s[i])
    ext_sinc_arr.append(k)
    
plt.plot(freq_s,ext_sinc_arr,'r',label='exact FT of sinc fun')    
plt.plot(freq_s,ft_s,'g',label='numerical FT')
plt.legend()
plt.show()
