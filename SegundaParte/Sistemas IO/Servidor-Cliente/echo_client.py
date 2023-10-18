import socket
import time

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # definicion de socket familia de socket , tipo de socket a recibir
    server_adress = ('localhost',5000)

    print(f"Conectando a servidor {server_adress[0]}:{server_adress[1]}")

    inicio = time.perf_counter()
    sock.connect(server_adress)

    try:
        msg = "Hola mundo!" # lo envia por bytes
        #print(f"Enviando mensaje: {msg}")
        sock.sendall(msg.encode('utf-8')) # algunos valores especiales dependen del tipo de codificación, entonces se tiene que
                                            # codificar en un formato antes de enviarlo (encoding)
        data = sock.recv(SOCK_BUFFER)
        #print(f"Recibido: {data}")
        
    finally:
        #print(f"Cerrando socket")
        socket.close
        fin = time.perf_counter()
        print(f"Recibido: {data}")
        print(f"el tiempo de ejecucion es {fin - inicio:e} segundos")


