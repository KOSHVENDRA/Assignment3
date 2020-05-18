"""
Calculating convoluion of Box function with itself
Author : Koshvendra Singh
Email  : koshvendra1999@gmail.com
Date   : 18/05/2020

"""

import numpy as np
import matplotlib.pyplot as plt

# defining Box function
def Box(x):
    y=np.zeros(len(x))
    for i in range(len(x)):
        if x[i]<1 and x[i]>-1:
            y[i]=1
        else:
            y[i]=0
    return (y)
    
xmin= -50
xmax= 50
numpoints=512

# sampling the function
x = np.linspace(xmin,xmax,numpoints)
dx=x[1]-x[0]
sample=Box(x)

# fourier tansform of box function
FT_box=np.fft.fft(sample)

#fixing factors
#freq=2*np.pi*np.fft.fftfreq(numpoints dx)
#factor=np.exp(-1j*freq*xmin)
#FT_box=dx*np.sqrt(numpoints/(2*np.pi))*factor*FT_box
FT_box=np.fft.fftshift(FT_box)

# multiply the two functions to be convoluted
mul= (FT_box)**2

# convolution of two functions
convol=np.fft.fftshift(np.fft.ifft(mul))

# convoluion using np.convolve function
num_convol=np.convolve(sample,sample,'same')

#plotting
plt.plot(x,np.real(convol),'g',label='without  convolve function')
plt.plot(x,num_convol,'r',label='using convolve function')
plt.plot(x,sample,'y',label='box function')
plt.legend()
plt.show()



