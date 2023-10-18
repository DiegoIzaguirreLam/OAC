
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

void llenaArreglo(int *arr,int N);
void cllenaIniFalt(int *arr,int *ini,int *falt,int N, int X);
int esPrimo(int num);

int main(){
    int N = 15, X = 10;
    int *arr, *ini, *falt;

    arr = (int*)malloc((N-1)*sizeof(int));
    ini = (int*)malloc((N-1)*sizeof(int));
    falt = (int*)malloc((N-1)*sizeof(int));

    llenaArreglo(arr,N);
    cllenaIniFalt(arr,ini,falt,N,X);

    for(int i=0;i<N-1;i++){
        printf("%d\t %d\t %d\n", arr[i],ini[i],falt[i]);
    }
    return 0;
}


void llenaArreglo(int *arr,int N){
    for(int i=2;i<=N;i++){
        arr[i-2] = i;
    }
}

void cllenaIniFalt(int *arr,int *ini,int *falt,int N, int X){
    int ultimoPrimo=0;
    for(int i=0;i<X-1;i++){
        if(esPrimo(arr[i])){
            ini[i] = 1;
            falt[i] = 0;
            for(int j=ultimoPrimo;j<i;j++)
                if(ini[j]==0) falt[j] = arr[i] - arr[j];
            ultimoPrimo = i;
        }
        else{
            ini[i] = 0;
            falt[i] = 0;
        }
    }
    for(int i=X-2;i<N-1;i++){
        ini[i] = 0;
        falt[i] = 0;
    }
}

int esPrimo(int num){
    for(int i=2;i<num;i++)
        if(num%i==0) return 0;
    return 1;
}
