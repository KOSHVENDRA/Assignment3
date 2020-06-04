# calculating fourier transform of constant function
# Author : Koshvendra Singh
# Email  : koshvendra1999@gmail.com
# Date   : 16/05/2020

import numpy as np
import matplotlib.pyplot as plt

const=float(input('Enter c for constant function f(x)=c\n'))
#No=int(input('enter no. of sample points : No\n'))

num=256
inp_arr=np.ones(num)*const   #  input array to be fourier transformed
xmin=-20
xmax=20
dx=(xmax-xmin)/(num-1)

dft=np.sqrt(num/(2*np.pi)) *(np.fft.fft(inp_arr,norm='ortho'))    # calculation of dft
freq= 2*np.pi*np.fft.fftfreq(num)                # frequency sample
factor=np.exp(-1j*freq*xmin)   
DFT=dx*factor*dft
dft_shift =np.fft.fftshift(DFT) 
freq_shift=np.fft.fftshift(freq)

plt.plot(freq_shift,dft_shift)

plt.show()
#print("dft of a constant function f(x)=c",dft)


