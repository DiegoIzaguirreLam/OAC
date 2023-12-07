import socket
import time

SOCK_BUFFER = 1024


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Conectando a servidor {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    try:
        ciudad = input("Ingrese el nombre de la Ciudad: ")
        N = input("Ingrese el N: ")
        msg = f"{N},{ciudad}"
        #print(f"Enviando mensaje: {msg}")
        ini = time.perf_counter()
        sock.sendall(msg.encode("utf-8"))
        data = sock.recv(SOCK_BUFFER)
        fin = time.perf_counter()
        tiempo_s = fin-ini
        ini = time.perf_counter()
        with open("ciudades.csv", "w") as f:
            f.write(data.decode())
        fin = time.perf_counter()
        tiempo_Es = fin-ini
        # print(f"Recibido: {data}")
    finally:  
        # print("Cerrando socket")
        sock.close()
    #print(f"Enviando mensaje: {msg}")
    print(f"El tiempo de recepcion de la data es de: {tiempo_s} segundos")
    print(f"El tiempo de escritura de la data es de: {tiempo_Es} segundos")

