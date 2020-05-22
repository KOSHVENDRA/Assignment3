#Author : Koshvendra Singh
# Email  : koshvendra1999@gmail.com
# Date   : 21/05/2020
# Description : the fourier transformation of 1d gaussian is done in c-code using FFTW , it's result printed in a file is to be plotted

import numpy as np
import matplotlib.pyplot as plt

data=np.genfromtxt('/home/koshvendra/Assignment_comp/Ass3_2020/gauss.txt',skip_header=0,skip_footer=0)
plt.plot(data[:,0],data[:,1],'r',label='using fftw')
plt.plot(data[:,0],data[:,2],'b.',label='analytical')
plt.legend()
plt.show()
