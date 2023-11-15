import socket
import time
from threading import Thread

SOCK_BUFFER = 1024

num_clientes = 0

def client_handler(connection, c_adress):
    global num_clientes
    num_clientes += 1
    print(f"Cliente conectado desde: {c_adress[0]}:{c_adress[1]}")
    print(f"Numero de clientes conectados: {num_clientes}")
    try: #lo usamos para que la conexión no se caiga
        while True:
            data = connection.recv(SOCK_BUFFER) # se queda esperando hasta que reciba data. a veces hay un timeout, donde retorna nulo si no recibe data
            if data:
                print(f"recibi {data}")
                connection.sendall(data)
                time.sleep(0.1)
            else:
                print(f"no hay mas datos de {c_adress[0]}:{c_adress[1]}")
                break
    except ConnectionError:
        num_clientes -= 1
        print(f"Cliente {c_adress[0]}:{c_adress[1]} desconectado abruptamente")
    finally:
        num_clientes -= 1
        connection.close()
        print(f"Conexion con {c_adress[0]}:{c_adress[1]} cerrada")


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_adress = ('localhost', 5000)

    print(f"Iniciando servidor en {server_adress[0]}:{server_adress[1]}")

    sock.bind(server_adress)

    print("Empezando a escuchar clientes...")
    sock.listen(4) #es como el numero de clientes que pueden estar "en cola" esperando para ser atendidos. 
                    # en este caso, mientras que se atiene 1, 1 está en la cola, entonces un tercer cliente no será atendido
    global num_clientes
    while True:
        conn, client_adress = sock.accept() #esto espera una conexion, bloquea el código hasta que haya una conexión. cuando haya una conexión,
                                            #retorna 
        t = Thread(target = client_handler, args = (conn, client_adress,)) # cuando recibe un cliente, genera un hilo y lo ejecuta
        t.start()
        num_clientes = num_clientes + 1
        print(f"Numero de clientes conectados: {num_clientes}")


if __name__ == '__main__':
    main()