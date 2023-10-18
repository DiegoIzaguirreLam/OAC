import socket

SOCK_BUFFER = 1024
# se envia un numero que equivale a la posicion donde esta el codigo y retorna el codigo. numero de linea

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # definicion de socket familia de socket , tipo de socket a recibir
    server_adress = ('localhost',5000)

    print(f"Conectando a servidor {server_adress[0]}:{server_adress[1]}")

    sock.connect(server_adress)

    try:
        msg = "10" # lo envia por bytes
        #print(f"Enviando mensaje: {msg}")
        sock.sendall(msg.encode('utf-8')) # algunos valores especiales dependen del tipo de codificación, entonces se tiene que
                                            # codificar en un formato antes de enviarlo (encoding)
        data = sock.recv(SOCK_BUFFER)
        num = int(data.decode('utf-8'))
        print(f"Recibido: {num}")
    finally:
        print(f"Cerrando socket")
        socket.close
        #print(f"Recibido: {indice}")


