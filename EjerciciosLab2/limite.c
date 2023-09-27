

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


double cFuncion(int n);
double asmFuncion(int n);

int main(){
	int n=1000000;
	srandom(time(NULL));

	struct timespec ti, tf;
	double elapsedC, elapsedASM, resultadoC, resultadoASM;
	clock_gettime(CLOCK_REALTIME, &ti);
    resultadoC = cFuncion(n);
    clock_gettime(CLOCK_REALTIME, &tf);
    elapsedC = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    printf("el tiempo en nanosegundos que toma la función en C es %lf\n", elapsedC);
	clock_gettime(CLOCK_REALTIME, &ti);
    resultadoASM = asmFuncion(n);
    clock_gettime(CLOCK_REALTIME, &tf);
    elapsedASM = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    printf("el tiempo en nanosegundos que toma la función en ASM es %lf\n", elapsedASM);
	printf("el resultado obtenido en C es de: %lf\n", resultadoC);
	printf("el resultado obtenido en ASM es de: %lf\n", resultadoASM);
	return 0;
}


double cFuncion(int n){
	return pow(1+(double)1/n, n);
}