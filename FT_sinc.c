/*
 *Description  : to compute the DFT of sinc function using FFTW
 * Compile it as   ' gcc FT_sinc.c -lfftw3 -lm -o sinc.out '
 */

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<complex.h>
#include<fftw3.h>

int main(){

  fftw_complex *sinc,*ft,*fts; 
  fftw_plan plan;
  double x,factor,freq;
  double R[]={-50,50};      // range for function to be defined in
  int num=256;                  // no. pf sample
  double dx=(R[1]-R[0])/(num-1);       // resolution in position space
  double pi=22.0/7.0;                // specifying of pi
  double df= 1/(num*dx);      //resolution in frequency space

  sinc=(fftw_complex*) fftw_malloc(sizeof(fftw_complex)*num);
  ft  =(fftw_complex*) fftw_malloc(sizeof(fftw_complex)*num);
  fts =(fftw_complex*) fftw_malloc(sizeof(fftw_complex)*num);
  

  // sampling the function
  for(int i=1;i<num;i++){
    ;
    x=(i*dx)+R[0];
    if (x==0){
      sinc[i]=1;
    }
    else{
      sinc[i]=sin(x)/x;

    }
    
  }
 
  
  plan=fftw_plan_dft_1d(num,sinc,ft,FFTW_FORWARD,FFTW_ESTIMATE);
  fftw_execute(plan);

  // Shifting fourier transform 
  for(int i=0;i<num/2;i++){

    
    fts[i]=( dx/(pow(2*pi,0.5)) )*ft[i+num/2];    
    fts[i+(num/2)]=(dx/(pow(2*pi,0.5)) )*ft[i];
  }
  FILE *file;
  int st=remove("sinc.txt");
  file=fopen("sinc.txt","w+");


    //printing fourier frequency and transform data in sinc.txt

  for (int i=0;i<num;i++){
    freq=2*pi*((i-(num/2))*df);      //frequency in transformed state
    factor=cos(-1*freq*R[0])+I*sin(-1*freq*R[0]); //factors to be multiplied in FT

    fprintf(file,"%f    %f\n",freq,creal(fts[i]*factor));
      }

  //destroying the plan and freeing the pointers
  
  fftw_destroy_plan(plan);
  fftw_free(sinc);fftw_free(ft);fftw_free(fts);fclose(file);


  return(0);
}
