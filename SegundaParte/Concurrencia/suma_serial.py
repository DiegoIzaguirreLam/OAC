import time



if __name__ == '__main__':
    n = 10000000
    sum = 0
    ini = time.perf_counter()
    for i in range(1, 2*n, 2):
        sum += i
    fin = time.perf_counter()
    print(f"El resultado es {sum}")
    if(sum == pow(n,2)):
        print(f"La suma se valida")
    print(f"El tiempo de ejecución total es de {fin-ini} segundos")

