
int main(){
	int N = 15, X = 10, *arr, *ini, *falt;

	arr = (int*)malloc((N-1)*sizeof(int));
	ini = (int*)malloc((N-1)*sizeof(int));
	falt = (int*)malloc((N-1)*sizeof(int));
	llenarArreglo(arr,N);
	cLlenaIniFalt(arr,ini,falt,X);
	asmLlenaIniFalt(arr,ini,falt,X);

	for(int i=0;i<N-1;i++){
		printf("%d \t %d \t %d\n",arr[i],ini[i],falt[i]);
	}
	return 0;
}

void llenarArreglo(int *arr,int N){
	for(int i=2;i<=N;i++){
		arr[i-2] = i;
	}
}

void cLlenaIniFalt(int *arr,int *ini, int *falt, int X){
	int i;
	for(i=0;i<X;i++){
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



