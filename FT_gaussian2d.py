# Finding  fourier transform of 2 dimensional gaussian function
# Author : Koshvendra Singh
# Email  : koshvendra1999@gmail.com
# Date   : 17/05/2020

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator,FormatStrFormatter


# defining 2D gaussian function
def Gauss(x,y):
    return np.exp(-((x**2)+(y**2)))

numpoints=32
xmin=-10
xmax=10

x1= np.linspace(xmin,xmax,numpoints)
y1=x1

dx=x1[1]-x1[0]        # resolution in x space

# creating 2D meshgrid on which function has to be evaluated
xm,ym=np.meshgrid(x1,y1)

# evaluation of gaussian function at grid points
Z=Gauss(xm,ym)

# calculating 2D fourier transform of gaussian function
FT_2d=np.fft.fft2(Z,norm='ortho')
FT_2d=np.fft.fftshift(FT_2d)

# getting frequency sample
freq1=np.fft.fftfreq(FT_2d.shape[0],dx)
freq1=np.fft.fftshift(freq1)
freq2=np.fft.fftfreq(FT_2d.shape[1],dx)
freq2=np.fft.fftshift(freq2)

# fixing the factors
freq1=2*np.pi*freq1
freq2=2*np.pi*freq2

factor1=np.exp(-1j*freq1*xmin)
factor2=np.exp(-1j*freq2*xmin)

# Ft after fixing the factors
FT_2d_fix=( (dx*np.sqrt(numpoints/(2*np.pi)))**2 )*factor1*factor2*FT_2d


# making meshgrid of frequency sample
freq_1,freq_2=np.meshgrid(freq1,freq2)

# Analytical Fourier transform of 2d gaussian function
Ana_ft=0.5*Gauss((freq_1)/2,(freq_2)/2)


# plotting
fig=plt.figure()
ax=fig.gca(projection='3d')
srf=ax.plot_surface(freq_1,freq_2,np.absolute(FT_2d_fix))
surf=ax.plot_surface(freq_1,freq_2,Ana_ft)
ax.set_xlabel('freq_1')
ax.set_ylabel('freq_2')
ax.set_zlabel('fourier transform')
plt.show()





