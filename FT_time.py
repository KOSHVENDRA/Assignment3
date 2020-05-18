# Comparison of time taken by the execution of self made code and numpy.fft.fft function for calculation of fourier transform
# Author : Koshvendra Singh
# Date   : 16/05/2020
# Email  : koshvendra1999@gmail.com

import numpy as np
import matplotlib.pyplot as plt
import time

# Defining a function to compute Fourier transform of N numbers
def DFT(x):
    x=np.asarray(x,dtype=float)
    N=x.shape[0]                   # gives no.of elements in input array
    n=np.arange(N)
    k=n.reshape((N,1))
    M=np.exp((-1j*2*np.pi*k*n)/N)
    return (1/np.sqrt(N))* np.dot(M,x)              # gives normalised DFT of input list x


my_time=[]                  # array for time taken by my code
np_time=[]                  # array for time taken by np.fft.fft function
n_arr=[]                    # its elements give no. of element in x each time

for i in range(97):
    x=np.random.random(i+4)
    
    start1_time=time.time()
    my_dft=DFT(x)           # calculate dft using my code
    end1_time=time.time()
    my_time.append(end1_time-start1_time)   # time during execution of my code

    start2_time=time.time()
    np_dft=np.fft.fft(x,norm="ortho")       # calculate dft by numpy function
    end2_time=time.time()
    np_time.append(end2_time-end2_time) # time during execution of np.fft.fft function

    n_arr.append(i+4)

plt.plot(n_arr,my_time,'g',label='time taken by my code')
plt.plot(n_arr,np_time,'r',label='time taken by np.fft.fft function')
plt.xlabel('N')
plt.ylabel('time(second)')
plt.legend()
plt.show()
    
