import random
import time

def genera_practicas():
    with open("notas_practicas.csv","w+") as f:
        codigo_inicial = 20230001
        cabecera = "codigo,p1,p2,p3,p4\n"
        f.write(cabecera)
        for i in range(200):
            codigo = codigo_inicial + i
            p1 = random.randint(0,20)
            p2 = random.randint(0,20)
            p3 = random.randint(0,20)
            p4 = random.randint(0,20)
            linea = f"{codigo},{p1},{p2},{p3},{p4}\n"
            f.write(linea)

def genera_labs():
    with open("notas_laboratorios.csv","w+") as f:
        codigo_inicial = 20230001
        cabecera = "codigo,l1,l2,l3,l4,l5\n"
        f.write(cabecera)
        for i in range(200):
            codigo = codigo_inicial + i
            l1 = random.randint(0,20)
            l2 = random.randint(0,20)
            l3 = random.randint(0,20)
            l4 = random.randint(0,20)
            l5 = random.randint(0,20)
            linea = f"{codigo},{l1},{l2},{l3},{l4},{l5}\n"
            f.write(linea)

def genera_parcial():
    with open("notas_parcial.csv", "w+") as f:
        codigo_inicial = 20230001
        cabecera = "codigo,e1"
        f.write(cabecera)
        for i in range(200):
            codigo = codigo_inicial + i
            e1 = random.randint(0,20)
            linea = f"{codigo},{e1}\n"
            f.write(linea)

def genera_final():
    with open("notas_final.csv", "w+") as f:
        codigo_inicial = 20230001
        cabecera = "codigo,e2"
        f.write(cabecera)
        for i in range(200):
            codigo = codigo_inicial + i
            e2 = random.randint(0,20)
            linea = f"{codigo},{e2}\n"
            f.write(linea)

if __name__ == '__main__':
    ini = time.perf_counter()
    genera_practicas()
    genera_labs()
    genera_parcial()
    genera_final()
    fin = time.perf_counter()
    print(f"El tiempo de ejecucion es de: {fin-ini} segundos")