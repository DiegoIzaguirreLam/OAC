


#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


extern void asmHallaDistancias(double *longitud, double *latitud, int cant, double *distancia, double multiplicador);
void cHallaDistancias(double *longitud, double *latitud,int cant, double *distancia, double multiplicador);

int main(){
	srandom(time(NULL));
	double longitud[] ={-12.0464, -13.5319, -16.409, -8.115, -6,7736};
	double latitud[] = {-77.0428, -71.9675, -71.5375, -79.0294, -79.8444};
	int cant = 5, multiplicador=110;
	double distancia[10] = {0};
	struct timespec ti, tf;
	double elapsedASM, elapsedC, SUp;

	clock_gettime(CLOCK_REALTIME, &ti);
	cHallaDistancias(longitud, latitud, cant, distancia, multiplicador);
	clock_gettime(CLOCK_REALTIME, &tf);
	elapsedC = (tf.tv_sec - ti.tv_sec)*1e9 + (tf.tv_nsec - ti.tv_nsec);
	printf("El tiempo en nano segundos que toma la función en C es %lf\n", elapsedC);

	for(int i=0;i<cant-1;i++)
		printf("Distancia %d %.2lf\n", i+1, distancia[i]);

	clock_gettime(CLOCK_REALTIME, &ti);
	asmHallaDistancias(longitud, latitud, cant, distancia, multiplicador);
	clock_gettime(CLOCK_REALTIME, &tf);
	elapsedASM = (tf.tv_sec - ti.tv_sec)*1e9 + (tf.tv_nsec - ti.tv_nsec);
	printf("El tiempo en nano segundos que toma la función en ASM es %lf\n", elapsedASM);
	for(int i=0;i<cant-1;i++)
			printf("Distancia %d %.2lf\n", i+1, distancia[i]);

	SUp = elapsedC/elapsedASM;
	printf("El SpeedUp del tiempo de ejecución del programa en ASM con respecto a C es de: %lf\n", SUp);
}



void cHallaDistancias(double *longitud, double *latitud,int cant, double *distancia, double multiplicador){
	double longLima=longitud[0], latLima=latitud[0];

	for(int i=1;i<cant;i++)
		distancia[i-1] = sqrt(pow(longLima-longitud[i], 2)+pow(latLima-latitud[i], 2)) * multiplicador;
}




