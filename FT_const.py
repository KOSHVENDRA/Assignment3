# calculating fourier transform of constant function
# Author : Koshvendra Singh
# Email  : koshvendra1999@gmail.com
# Date   : 16/05/2020

import numpy as np
import matplotlib.pyplot as plt

const=float(input('Enter c for constant function f(x)=c\n'))
No=int(input('enter no. of sample points : No\n'))

inp_arr=np.ones(No)*const   #  input array to be fourier transformed

dft=np.sqrt(No/(2*np.pi)) *(np.fft.fft(inp_arr,norm='ortho'))    # calculation of dft
dft_shift=np.fft.fftshift(dft)

freq= 2*np.pi*np.fft.fftfreq(No)                # frequency sample
freq_shift=np.fft.fftshift(freq)

plt.plot(freq_shift,dft_shift)

plt.show()
#print("dft of a constant function f(x)=c",dft)


