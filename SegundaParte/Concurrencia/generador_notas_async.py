import aiofiles
import asyncio
import random
import time

async def genera_practicas():
    async with aiofiles.open("notas_practicas.csv", "w+") as f:
        codigo_inicial = 20230001
        cabecera = "codigo,p1,p2,p3,p4\n"
        await f.write(cabecera)
        for i in range(200):
            codigo = codigo_inicial + i
            p1 = random.randint(0,20)
            p2 = random.randint(0,20)
            p3 = random.randint(0,20)
            p4 = random.randint(0,20)
            linea = f"{codigo},{p1},{p2},{p3},{p4}\n"
            await f.write(linea)

async def genera_labs():
    async with aiofiles.open("notas_laboratorios.csv","w+") as f:
        codigo_inicial = 20230001
        cabecera = "codigo,l1,l2,l3,l4,l5\n"
        await f.write(cabecera)
        for i in range(200):
            codigo = codigo_inicial + i
            labs = [random.randint(0,20) for _ in range (5)]
            linea = f"{codigo},{','.join(map(str,labs))}\n"
            await f.write(linea)

async def genera_parcial():
    async with aiofiles.open("notas_parcial.csv", "w+") as f:
        codigo_inicial = 20230001
        cabecera = "codigo,nota\n"
        await f.write(cabecera)
        for i in range(200):
            codigo = codigo_inicial + i
            e1 = random.randint(0,20)
            linea = f"{codigo},{e1}\n"
            await f.write(linea)

async def genera_final():
    async with aiofiles.open("notas_final.csv", "w+") as f:
        codigo_inicial = 20230001
        cabecera = "codigo,nota\n"
        await f.write(cabecera)
        for i in range(200):
            codigo = codigo_inicial + i
            e2 = random.randint(0,20)
            linea = f"{codigo},{e2}\n"
            await f.write(linea)

async def main():
    await asyncio.gather(genera_practicas(), genera_labs(), genera_parcial(), genera_final())

if __name__ == '__main__':
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()
    print(f"El tiempo de ejecucion es de {fin-inicio} segundos")
