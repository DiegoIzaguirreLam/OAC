
import time

if __name__ == '__main__':
    inicio = time.perf_counter()
    with open("archivo.txt", "r", encoding='utf-8') as f:
        codigo = f.read()
        print(codigo, end="")
    fin = time.perf_counter()
    print(f"el tiempo de ejecucion es {fin - inicio:e} segundos")

