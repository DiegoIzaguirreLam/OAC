import time
import numpy as np
import random
from memory_profiler import profile

@profile
def minimo_elementos_sync(A,B,ABm):
    for i in range(len(A)):
        ABm.append(min(A[i], B[i]))

if __name__ == '__main__':
    N = 4096
    A = [random.randint(0,100) for _ in range(N)]
    B = [random.randint(0,100) for _ in range(N)]
    ABm = []
    ini = time.perf_counter()
    minimo_elementos_sync(A,B,ABm)
    fin = time.perf_counter()
    #print(f"El resultado es: {ABm}\n")
    print(f"El tiempo de ejecucion es de {fin-ini} segundos")


