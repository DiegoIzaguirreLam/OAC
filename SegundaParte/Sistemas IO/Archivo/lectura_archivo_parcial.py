

import time
#tarea, buscar como hacer para que no se tenga que usar un for, pero un while verificando fin de archivo


if __name__ == '__main__':
    inicio = time.perf_counter()
    contenido = ""
    with open("archivo.txt","r",encoding="utf-8") as f:
        for i in range(50):
            contenido += f.readline()
    fin = time.perf_counter()
    print(contenido)
    print(f"tiempo de ejecucion: {fin-inicio:e} segundos") #leer todo de una es más rápido

