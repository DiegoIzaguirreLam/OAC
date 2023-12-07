import time
from multiprocessing import Pool, cpu_count
import random
from memory_profiler import profile

N= 4096
A = [random.randint(0,100) for _ in range(N)]
B = [random.randint(0,100) for _ in range(N)]

@profile
def operacion_minimo(i):
    return min(A[i], B[i])

if __name__ == '__main__':
    ABm = list()
    ini = time.perf_counter()
    with Pool(processes=cpu_count()) as pool:
        ABm = pool.map(operacion_minimo, range(len(A)))
    fin = time.perf_counter()
    #print(f"El resultado es de: {ABm}\n")
    print(f"El tiempo de ejecucion es de : {fin-ini} segundos")