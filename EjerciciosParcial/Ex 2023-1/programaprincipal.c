


#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

extern void asmLlenaIniFalt(int *arr,int *ini, int *falt, int X);
void llenarArreglo(int *arr,int N);
void cLlenaIniFalt(int *arr,int *ini, int *falt, int X);
int esPrimo(int num);


int main(){
	int N = 15, X = 12, *arr, *ini, *falt;
	struct timespec ti, tf;
    double elapsedC, elapsedASM;

	arr = (int*)malloc((N-1)*sizeof(int));
	ini = (int*)malloc((N-1)*sizeof(int));
	falt = (int*)malloc((N-1)*sizeof(int));
	llenarArreglo(arr,N);
	clock_gettime(CLOCK_REALTIME, &ti);
	cLlenaIniFalt(arr,ini,falt,X);
	clock_gettime(CLOCK_REALTIME, &tf);
	elapsedC = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
	printf("Resultados C:\n");
	for(int i=0;i<N-1;i++){
		printf("%d \t %d \t %d\n",arr[i],ini[i],falt[i]);
	}
	clock_gettime(CLOCK_REALTIME, &ti);
	asmLlenaIniFalt(arr,ini,falt,X);
	clock_gettime(CLOCK_REALTIME, &tf);
	elapsedASM = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
	printf("Resultados ASM:\n");
	for(int i=0;i<N-1;i++){
		printf("%d \t %d \t %d\n",arr[i],ini[i],falt[i]);
	}
	printf("El tiempo de ejecucion de la función en C es de: %.2lf\n",elapsedC);
	printf("El tiempo de ejecucion de la función en ASM es de: %.2lf\n",elapsedASM);
	return 0;
}

void llenarArreglo(int *arr,int N){
	for(int i=2;i<=N;i++){
		arr[i-2] = i;
	}
}

void cLlenaIniFalt(int *arr,int *ini, int *falt, int X){
	int i;
	for(i=0;i<X-2;i++){
		if(esPrimo(arr[i])){
			ini[i] = 1;
			falt[i] = 0;
			for(int j=0;j<i;j++)
				if(!ini[j] && !falt[j]) falt[j] = arr[i] - arr[j];
		}
		else{
			ini[i] = 0;
			falt[i] = 0;
		}
	}
}

int esPrimo(int num){
	for(int i=2;i<num;i++)
		if(num%i==0) return 0;
	return 1;
}
