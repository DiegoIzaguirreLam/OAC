import time
from threading import Thread

def count():
    idx = 100
    while idx > 0:
        print(f"{idx}")
        idx -= 1
        time.sleep(0.1)

if __name__ == '__main__':
    inicio = time.perf_counter()
    t1 = Thread(target = count)
    t2 = Thread(target = count)
    t3 = Thread(target = count)
    t4 = Thread(target = count)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    fin = time.perf_counter()

    print(f"El tiempo de ejecucion es de {fin - inicio} segundos")
