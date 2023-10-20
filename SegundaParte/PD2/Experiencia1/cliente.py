import socket
import time

SOCK_BUFFER = 1024
# se envia un numero que equivale a la posicion donde esta el codigo y retorna el codigo. numero de linea

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # definicion de socket familia de socket , tipo de socket a recibir
    server_adress = ('localhost',5000)

    print(f"Conectando a servidor {server_adress[0]}:{server_adress[1]}")

    sock.connect(server_adress)
    numempleados = input('Escriba el numero de empleados: ')
    try:
        msg = numempleados.encode() # lo envia por bytes
        #print(f"Enviando mensaje: {msg}")
        sock.send(msg) # algunos valores especiales dependen del tipo de codificación, entonces se tiene que
                                            # codificar en un formato antes de enviarlo (encoding)
        inicio = time.perf_counter()
        data = ''
        while True:
            raw = sock.recv(SOCK_BUFFER)
            if not raw:
                break
            data += raw.decode()
        with open("descarga.csv", "w") as f:
            f.write(f"{data}")
        fin = time.perf_counter()
        t = (fin - inicio)*1000
        print(f"Tiempo de escritura {t:.3f} ms")
    finally:
        print(f"Cerrando socket")
        socket.close
        #print(f"Recibido: {indice}")


