

#include <stdio.h>

#include <stdlib.h>
#include <math.h>
#include <time.h>


extern void asmHallaDistancias(float *,float *, float *, int ,float );
void cHallaDistancias(float *,float *, float *, int ,float );
void imprimeDistancias(const char *nombArch, float *dist,int cant);

int main(){
	FILE *arch;
	arch = fopen("ciudades.txt", "r");
	if(arch == NULL){
		printf("ERROR: no se pudo abrir el archivo ciudades.txt\n");
		exit(1);
	}
	int cant = 5;
	float longi[5], lat[5], dist[5], vlongi, vlat;
	struct timespec ti, tf;
    double elapsedC, elapsedASM;
    float convert=110;
	for(int i=0;i<cant;i++){
		while(fgetc(arch)!='\n');
		fscanf(arch, "%f, %f\n", &vlongi, &vlat);
		printf("%f, %f\n", vlongi, vlat);
		longi[i] = vlongi;
		lat[i] = vlat;
 	}
	clock_gettime(CLOCK_REALTIME, &ti);
    cHallaDistancias(longi,lat,dist,cant,convert);
    clock_gettime(CLOCK_REALTIME, &tf);
	elapsedC = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    printf("el tiempo en nanosegundos que toma la función en C es %lf\n", elapsedC);
    imprimeDistancias("distanciasC.txt",dist, cant);

	clock_gettime(CLOCK_REALTIME, &ti);
    asmHallaDistancias(longi,lat,dist,cant,convert);
    clock_gettime(CLOCK_REALTIME, &tf);
	elapsedASM = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    printf("el tiempo en nanosegundos que toma la función en ASM es %lf\n", elapsedASM);
    imprimeDistancias("distanciasASM.txt",dist, cant);
}

void cHallaDistancias(float *longi,float *lat, float *dist, int cant,float convert){
	float longLima = longi[0], latLima = lat[0];
	for(int i=1;i<cant;i++){
		dist[i-1] = sqrt(pow(longLima-longi[i],2)+pow(latLima-lat[i],2)) * convert;
	}
}

void imprimeDistancias(const char *nombArch, float *dist,int cant){
	FILE *arch;
	arch = fopen(nombArch, "w");
	if(arch == NULL){
		printf("error al abrir %s\n", nombArch);
		exit(1);
	}
	for (int i=0;i<cant-1;i++)
		fprintf(arch, "Distancia %d: %.5f\n", i+1, dist[i]);
	fclose(arch);
}




