/* 
* Author : Koshvendra Singh
* Email  : koshvendra.singh@tifr.res.in
* Date   : 18/05/2020
* Description : C code for computing fourier transform(FT) of gussian function  using FFTW
and then plotting is done in python.
* compile using "gcc FT_gaussian.c -lfftw3 -lm -o gauss.out "  
*/

#include<stdio.h>
#include<stdlib.h>
#include<complex.h>
#include<fftw3.h>
#include<math.h>


int main () {
  
  double x,freq,An_ft,l;
  fftw_complex *gauss,*ft_gauss,*ft_gauss_s ;
  fftw_plan plan;
  int num = 512;   //   no. of points function to be calculated at
  double R[]={-25,25};      //  range of x axis
  double pi=22.0/7.0  ;
  double dx=(R[1]-R[0])/(num-1);  // resolution in x space
  double df=1/(num*dx) ;  //resolution in frequency space

  // memory allocation 
  gauss = (fftw_complex*) fftw_malloc(sizeof(fftw_complex)*num);
  ft_gauss=(fftw_complex*) fftw_malloc(sizeof(fftw_complex)*num);
  ft_gauss_s=(fftw_complex*) fftw_malloc(sizeof(fftw_complex)*num);

  double *Ana_ft=(double*) malloc(sizeof(double)*num);
  ///double *freq=(double*) malloc(sizeof(double)*num)
  /// double *freq=(double*) malloc(sizeof(double)*num);

 
  // sampling of function
  for(int i=0;i<num;i++)
    {
    x=(i*dx) + R[0];
    gauss[i] = exp(-1*x*x);

  }

  // Computing fourier transform
  plan=fftw_plan_dft_1d(num,gauss,ft_gauss,FFTW_FORWARD,FFTW_ESTIMATE);
  fftw_execute(plan);

  // shifting the sample of FT s.t. zero frequency term comes in center
  fftw_complex k;
  for (int i=0;i<num/2;i++)
    {
    k=ft_gauss[i];
    ft_gauss_s[i] = ft_gauss[i+num/2];
    ft_gauss_s[i+num/2]=k;
  }

  // Analytical fourier transform : 0.5*exp(-k*k/2)
  // getting an array of analytical solution and array of frequency
  //for (int i=0;i<num;i++){
  //freq[i]=2*pi*(i-(num/2))*df;
  //Ana_ft[i]=(pow(2,0.5))*exp(-(freq[i]*freq[i])/4);
  //}

  // file to save data of the result
  FILE *file;
  int st=remove("gauss.txt");
  file= fopen("gauss.txt","w+");
  

  // taking the data on the file
  fftw_complex factor;
  for (int i=0;i<num;i++)
    {
    freq=2*pi*(i-(num/2))*df;
    factor=cos(-1*freq*R[0])+ I*sin(-1*freq*R[0]);
    An_ft=(1/(pow(2,0.5)))*exp(-1*(freq*freq)/4);
    l=(dx/ (pow(2*pi,0.5)) );
    fprintf(file,"%f    %f    %f\n",freq,l*creal(factor*ft_gauss_s[i]), An_ft);
  }

  //destroying the plan and freeing the pointers
  fftw_destroy_plan(plan);
  fftw_free(gauss);
  fftw_free(ft_gauss);
  fftw_free(ft_gauss_s);

  return(0);
}
	    
      
	    
      
	    
    
				    
  
      
    
      
    
    
      
      

  
    
    
