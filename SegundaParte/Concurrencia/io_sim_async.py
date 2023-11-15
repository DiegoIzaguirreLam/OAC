import asyncio
import time

async def func1(): #lo convierte en una corutina
    print("Funcion 1 empezando")
    await asyncio.sleep(2) #este es asincrono, permite que entre a otra subrutina mientras espera
    print("Funcion 1 terminando")

async def func2():
    print("Funcion 2 empezando")
    await asyncio.sleep(3)
    print("Funcion 2 terminando")

async def func3():
    print("Funcion 3 empezando")
    await asyncio.sleep(1)
    print("Funcion 3 terminando")

async def main():
    await asyncio.gather(func1(),func2(),func3()) #va a juntar todas las corutinas y las va a mandar a ejecutar a la vez (en el loop)
    #se queda esperando que terminen. bloquea el codigo. el gather retorna una lista con lo que retornan las funciones (en orden)

if __name__ == '__main__':
    inicio = time.perf_counter()
    asyncio.run(main()) #run manda a ejecutar la corutina y espera que termine. se esta lidiando con una sola corutina en ese momento
    fin = time.perf_counter()
    print(f"Tiempo total de ejecución: {fin-inicio} segundos")
 


