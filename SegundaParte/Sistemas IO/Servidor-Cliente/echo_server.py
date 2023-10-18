import socket

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_adress = ('localhost', 5000)

    print(f"Iniciando servidor en {server_adress[0]}:{server_adress[1]}")

    sock.bind(server_adress)

    print("Empezando a escuchar clientes...")
    sock.listen(1) #es como el numero de clientes que pueden estar "en cola" esperando para ser atendidos. 
                    # en este caso, mientras que se atiene 1, 1 está en la cola, entonces un tercer cliente no será atendido


    while True:
        conn, client_adress = sock.accept() #esto espera una conexion, bloquea el código hasta que haya una conexión. cuando haya una conexión,
                                            #retorna 
        print(f"Cliente conectado desde: {client_adress[0]}:{client_adress[1]}")

        try: #lo usamos para que la conexión no se caiga
            while True:
                data = conn.recv(SOCK_BUFFER) # se queda esperando hasta que reciba data. a veces hay un timeout, donde retorna nulo si no recibe data
                if data:
                    print(f"recibi {data}")
                    conn.sendall(data)
                else:
                    print(f"no hay mas datos de {client_adress[0]}:{client_adress[1]}")
                    break
        except ConnectionError:
            print(f"Cliente {client_adress[0]}:{client_adress[1]} desconectado abruptamente")
        finally:
            conn.close()
            print(f"Conexion con {client_adress[0]}:{client_adress[1]} cerrada")



