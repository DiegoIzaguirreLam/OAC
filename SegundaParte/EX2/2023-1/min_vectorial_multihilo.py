import time
from concurrent.futures import ThreadPoolExecutor
import random
from memory_profiler import profile


N = 4096
A = [random.randint(0,100) for _ in range(N)]
B = [random.randint(0,100) for _ in range(N)]
ABm = [0] * len(A)

@profile
def operacion_minimo(i):
    ABm[i] = min(A[i], B[i])



def main():
    workers = 8
    ini = time.perf_counter()
    
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for i in range(len(A)):
            executor.submit(operacion_minimo, i)
    fin = time.perf_counter()
    #print(f"El resultado es de: {ABm}\n")
    print(f"El tiempo de ejecucion es de : {fin-ini} segundos")

if __name__ == '__main__':
    main()
    