"""
Author : Koshvendra Singh
Email  : koshvendra.singh@tifr.res.in
Discription : Code for Fourier transform of sinc function in 'c' using FFTW library is written ,it's result is matched by similar computation in python using numpy.fft.fft

"""

# copying the Fourier transform code of sinc function written in python from question 1

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
    


# importing the sinc.txt file which we got by coding the FT in c

import_data=np.genfromtxt('/home/koshvendra/Assignment_comp/Ass3_2020/sinc.txt',skip_header=0,skip_footer=0)

# plotting the numpy and c-code result 
plt.plot(freq_s,ext_sinc_arr,'r',label='exact FT of sinc fun')    
plt.plot(freq_s,ft_s,'g',label='reult from python-code')
plt.plot(import_data[:,0],import_data[:,1],'b',label='result from c-code')
plt.legend()
plt.show()


