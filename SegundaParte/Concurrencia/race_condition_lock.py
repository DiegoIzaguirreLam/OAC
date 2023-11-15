import time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = Lock()

    def update(self, name):
        print(f"Thread {name}: Iniciando actualizacion")
        print(f"Thread {name}: a punto de adquirir el valor")
        with self._lock:
            print(f"Thread {name}: ha adquirido el lock")
            local_copy = self.value
            local_copy = local_copy + 1
            time.sleep(0.1)
            self.value = local_copy
            print(f"Thread {name}: a punto de liberar el lock")
        print(f"Thread {name}: ha liberado el lock")
        print(f"Thread {name}: Finalizando actualizacion")
    

if __name__ == '__main__':
    worker = 5
    db = FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")
    
    with ThreadPoolExecutor(max_workers=worker) as executor: # va a crear un pool de hilos
        for index in range(worker):
            executor.submit(db.update, index) # se pone en cola la tarea. el pool le va a asignar una tarea a un hilo.
            #cuando se tienen más tareas que hilos, entonces se ejecutan tantas como hilos hallan primero y luego se ejecutan las otras.
            # la idea es que se tengan mas tareas por ejecutar que hilos: tener una cantidad limitada de recursos que ejecuten esa cantidad de tareas.






    print(f"Valor final de la base de datos: {db.value}")


