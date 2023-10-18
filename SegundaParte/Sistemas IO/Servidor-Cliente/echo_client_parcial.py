import socket
import time

SOCK_BUFFER = 4


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # definicion de socket familia de socket , tipo de socket a recibir
    server_adress = ('localhost',5000)

    print(f"Conectando a servidor {server_adress[0]}:{server_adress[1]}")

    inicio = time.perf_counter()
    sock.connect(server_adress)

    try:
        msg = "Hola mundo!" # lo envia por bytes
        #print(f"Enviando mensaje: {msg}")
        data = b"" # el b identifica que ese string no es un string sino una secuencia de bytes
        times = len(msg.encode('utf-8'))//SOCK_BUFFER + 1
        for i in range(times):
            men = msg[SOCK_BUFFER*i:SOCK_BUFFER*(i+1)]
            sock.sendall(men.encode('utf-8')) # algunos valores especiales dependen del tipo de codificación, entonces se tiene que
                                                # codificar en un formato antes de enviarlo (encoding)
            partial_data = sock.recv(SOCK_BUFFER) # la data esta en bytes
            data += partial_data
            #print(f"Recibido: {partial_data}")
        #print(f"Recibido: {data}")
        
    finally:
        #print(f"Cerrando socket")
        socket.close
        fin = time.perf_counter()
        print(f"Recibido: {data}")
        print(f"el tiempo de ejecucion es {fin - inicio:e} segundos")


