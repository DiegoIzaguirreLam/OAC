import time

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
    func1()
    func2()
    func3()

if __name__ == '__main__':
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()
    print(f"Tiempo total de ejecución: {fin-inicio} segundos") 