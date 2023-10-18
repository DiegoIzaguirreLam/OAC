
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>



float cCalculaVar(float *arr, int n);
extern float asmCalculaVar(float *arr, int n);


int main (){
	
	float arr[10] = {2,7,3,12,9};
	int n=5;
	struct timespec ti, tf;
	double elapsedC, elapsedASM;
	float varC, varAsm;

	clock_gettime(CLOCK_REALTIME, &ti);
	varC = cCalculaVar(arr, n);
	clock_gettime(CLOCK_REALTIME, &tf);
	elapsedC = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);

	clock_gettime(CLOCK_REALTIME, &ti);
	varAsm = asmCalculaVar(arr, n);
	clock_gettime(CLOCK_REALTIME, &tf);
	elapsedASM = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);

	printf("La varianza segun C es de: %f\n", varC);
	printf("La varianza segun ASM es de: %f\n", varAsm);
	printf("El tiempo en nanosegundos que toma la función en C es de: %lf\n", elapsedC);
	printf("El tiempo en nanosegundos que toma la función en ASM es de: %lf\n", elapsedASM);
	double speedUp = elapsedC/elapsedASM;
	printf("El SpeedUp de ASM con respecto a C es de: %lf\n", speedUp);
}

float cCalculaVar(float *arr, int n){
	float var=0, media=0;
	for(int i=0;i<n;i++)
		media += arr[i];
	media/=n;
	for(int i=0;i<n;i++)
		var += pow(arr[i]-media, 2);
	var/=n;
	return var;
}
