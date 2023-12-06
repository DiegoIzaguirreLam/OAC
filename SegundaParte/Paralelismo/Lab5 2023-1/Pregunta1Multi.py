
from multiprocessing import cpu_count, Pool

def calcular_sumatoria_multi(ini, fin) -> int:
    suma = 0
    for i in range(ini, fin+1, 2):
        suma += i
    #print(f"Suma: {suma}")
    return suma
    

def suma_paralela(n, num_procesos):
    terminos_por_proceso = n // num_procesos
    inicio = 1
    fin = 1 + (terminos_por_proceso*2 - 1)
    args = []
    while fin <= 2*n:
        args.append((inicio,fin))
        inicio = fin + 1
        fin = inicio + (terminos_por_proceso * 2 - 1)
    with Pool(processes=num_procesos) as pool:
        resultados = pool.starmap(calcular_sumatoria_multi, args)
    return sum(resultados)
    
if __name__ == '__main__':
    #lista_n = [1000000000, 500000000, 100000000, 10000000, 1000000]
    lista_n = [1000000]
    #lista_n = [100000000, 10000000, 1000000]
    resultados = []
    for n in lista_n:
        resultado = suma_paralela(n, num_procesos=cpu_count())
        
        if(resultado==pow(n,2)):
            print(f"Se valida la suma")
        

