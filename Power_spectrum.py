
#Author : Koshvendra Singh
#Email  : koshvenda1999@gmail.com
#Date   : 18/05/2020
#To study the power spectrum of a given data


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc

# reading noise file
Data=np.genfromtxt('/home/koshvendra/Assignment_comp/Ass3_2020/noise.txt',skip_header=0,skip_footer=0)

# aaray for  ith number of observation
x=np.arange(0,len(Data),1)

# plotting the noise
plt.plot(x,Data)
plt.title('Noise Data')
plt.xlabel('observation number')
plt.ylabel('noise')
plt.show()

# Calculating the Fourier transform of the Noise data
FT_noise=np.sqrt(len(Data)/(2*np.pi))*(np.fft.fft(Data,norm='ortho'))
FT_noise=np.fft.fftshift(FT_noise)

freq=2*np.pi*(np.fft.fftfreq(len(Data)))
freq=np.fft.fftshift(freq)

#plotting Fourier transform
plt.plot(freq,np.real(FT_noise))
plt.title('Fourier transform of noise data')
plt.xlabel('frequency')
plt.ylabel('fourier transform')
plt.show()

# calculating discrete power spectrum using Periodogram
Power_spect=(1/len(Data))*(np.absolute(FT_noise))**2

#plotting power spectrum
plt.plot(freq,Power_spect)
plt.xlabel('freq')
plt.ylabel('power spectrum')
plt.title('Power spectrum of noise')
plt.show()

# binned power spectrum and plotting
bin_mean,bin_edges,binnumber=sc.binned_statistic(freq,Power_spect,statistic='mean',bins=10)

bin_ed=[]
for i in range(len(bin_edges)-1):
    l=(bin_edges[i+1]+bin_edges[i])/2
    bin_ed.append(l)

plt.bar(bin_ed,bin_mean,width=(bin_edges[1]-bin_edges[0]))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.xlabel('frequency')
plt.ylabel('binned power spectrum')
plt.title('binned Power Spectrum')
plt.show()
