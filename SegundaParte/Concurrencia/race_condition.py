import time
from concurrent.futures import ThreadPoolExecutor

class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        print(f"Thread {name}: Iniciando actualizacion")
        local_copy = self.value
        local_copy = local_copy + 1
        time.sleep(0.1)
        self.value = local_copy
        print(f"Thread {name}: Finalizando actualizacion")


if __name__ == '__main__':
    worker = 5
    #tasks = worker * 2
    db = FakeDatabase()
    
    print(f"Valor inicial de la base de datos: {db.value}")
    
    with ThreadPoolExecutor(max_workers=worker) as executor: # va a crear un pool de hilos
        for index in range(worker):
            executor.submit(db.update, index) # se pone en cola la tarea. el pool le va a asignar una tarea a un hilo.
            #cuando se tienen más tareas que hilos, entonces se ejecutan tantas como hilos hallan primero y luego se ejecutan las otras.
            # la idea es que se tengan mas tareas por ejecutar que hilos: tener una cantidad limitada de recursos que ejecuten esa cantidad de tareas.






    print(f"Valor final de la base de datos: {db.value}")


