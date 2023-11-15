import socket
import time

SOCK_BUFFER = 1024


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Conectando a servidor {server_address[0]}:{server_address[1]}")

    inicio = time.perf_counter()
    sock.connect(server_address)

    try:
        for i in range(15):
            msg = f"Mensaje: {i+1}"
            print(f"Enviando mensaje: {msg}")
            sock.sendall(msg.encode("utf-8"))
            data = sock.recv(SOCK_BUFFER)
            #print(f"Recibido: {data}")
    finally:  
        # print("Cerrando socket")
        sock.close()
    fin = time.perf_counter()
    #print(f"Enviando mensaje: {msg}")
    print(f"Tiempo de ejecucion: {fin - inicio} segundos")