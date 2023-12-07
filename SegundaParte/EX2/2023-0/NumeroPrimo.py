
import math
import time
from multiprocessing import Pool
import matplotlib.pyplot as plt

def esPrimo(n) -> bool:
    fin = int(math.sqrt(n))+1
    for i in range(2,fin):
        if(n%i == 0):
            return False
    return True

def esPrimo_mult_rango(ini, fin, n) -> bool:
    for i in range(ini, fin+1):
        if(n%i == 0):
            return False
        #print(f"{i}")
    return True

def esPrimo_mult(n, num_procesos) -> bool:
    terminos = int(math.sqrt(n)) // num_procesos # 6
    inicio = 2
    fin = 2 + terminos
    args = []
    resultados = []
    while(fin <= math.sqrt(n)):
        args.append((inicio, fin, n))
        inicio = fin+1
        fin = inicio + terminos
    #print(f"{args}")
    with Pool(processes=num_procesos) as pool:
        resultados = pool.starmap(esPrimo_mult_rango, args)
    for resultado in resultados:
        if resultado == False:
            return False
    return True

if __name__ == '__main__':
    n = 2_345_678_911_111_111
    ini = time.perf_counter()
    resultado_A = esPrimo(n)
    fin = time.perf_counter()
    tiempo_a = fin-ini
    print(f"El tiempo de ejecucion es de: {fin-ini} segundos")
    ini = time.perf_counter()
    resultado_B = esPrimo_mult(n, num_procesos=2)
    fin = time.perf_counter()
    print(f"El tiempo de ejecucion es de: {fin-ini} segundos")
    tiempo_b = fin-ini
    assert(resultado_A == resultado_B)
    tiempos = []
    list_nprocesos = [1, 2, 4, 8, 16]
    for i in list_nprocesos:
        ini = time.perf_counter()
        resultado_B = esPrimo_mult(n, num_procesos=i)
        fin = time.perf_counter()
        tiempo = fin-ini
        tiempos.append(tiempo)
    
    plt.plot(list_nprocesos, tiempos)
    plt.ylabel("Tiempo de ejecución (s)")
    plt.xlabel("Número de procesos")
    plt.savefig('stats.png')

    

