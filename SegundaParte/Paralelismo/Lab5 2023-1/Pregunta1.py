from multiprocessing import cpu_count, Pool
import time

def calcular_sumatoria_sync(n) -> int:
    suma = 0
    for i in range(1, 2*n, 2):
        suma += i
    return suma

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
    lista_n = [1000000000, 500000000, 100000000, 10000000, 1000000]
    #lista_n = [100000000, 10000000, 1000000]
    
    with open("ResultadoPreg1.txt", "w") as f:
        f.write(f"Numero de procesos: #{cpu_count()}\n")
    for n in lista_n:
        ini = time.perf_counter()
        resultado_sync =calcular_sumatoria_sync(n)
        fin = time.perf_counter()
        t_serial = fin-ini
        ini = time.perf_counter()
        resultado_mult = suma_paralela(n, num_procesos=cpu_count())
        fin = time.perf_counter()
        t_paralela = fin-ini
        with open("ResultadoPreg1.txt","a") as f:
            f.write(f"Tiempo de ejecucion serial para {n}: {t_serial} segundos\n")
            f.write(f"Tiempo de ejecucion paralela para {n}: {t_paralela} segundos\n")
            f.write(f"SpeedUp: {t_serial/t_paralela}\n\n")
    

# La solucion paralela presenta un SpeedUp significativo para altos valores de n. Sin embargo, para valores
# más bajos de n se observa que la solución secuencial presenta mejores resultados en tiempo de ejecución
# esto se puede deber por diversos factores, principalmente debido a que para iniciar un nuevo proceso se deben
# realizar ciertas operaciones, las cuales toman tiempo. Por ejemplo, cada proceso independiente necesita su propio
# intérprete, que realiza ciertas operaciones como guardar los números de 0 a 255 en memoria, lo cuál toma un tiempo 
# adicional. Para valores bajos de "n", entonces, este tiempo parece ser mayor al tiempo que se optimiza a través de la 
# paralelización de la operación, resultando en un mayor tiempo de ejecución para el caso paralelo.
