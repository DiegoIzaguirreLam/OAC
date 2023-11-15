import time
from threading import Thread


def func1():
    print("Funcion 1 empezando")
    time.sleep(2) #tiempo de espera de segundos, bloquea el codigo 
    print("Funcion 1 terminando")


def func2():
    print("Funcion 2 empezando")
    time.sleep(3)
    print("Funcion 2 terminando")


def func3():
    print("Funcion 3 empezando")
    time.sleep(1)
    print("Funcion 3 terminando")

def main():
    t1 = Thread(target=func1)
    t2 = Thread(target=func2)
    t3 = Thread(target=func3)

    t1.start()
    t2.start()
    t3.start()

    t1.join() #detiene el hilo desde donde fue llamado hasta que termine. si no se pone esto, no va a esperar que terminen los hilos
    t2.join()
    t3.join()


if __name__ == '__main__':
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()
    print(f"Tiempo total de ejecución multi hilo: {fin-inicio} segundos")

