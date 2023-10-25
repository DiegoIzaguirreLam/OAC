import socket

SOCK_BUFFER = 1024


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_adress = ('localhost', 5001)

    print(f"Iniciando servidor en {server_adress[0]}:{server_adress[1]}")

    server_socket.bind(server_adress)

    print("Empezando a escuchar clientes...")
    server_socket.listen(1)

    while True:
        conn, client_adress = server_socket.accept()
        print(f"Cliente conectado desde: {client_adress[0]}:{client_adress[1]}")

        try:
            while True:
                raw = conn.recv(SOCK_BUFFER)
                if raw:
                    data = raw.decode()
                    mensaje = data.split(':')
                    print(f"Mensaje: {mensaje}")
                    if mensaje[0] == 'codigo':
                        cod = int(mensaje[1])
                        ind = cod - 20230000
                        with open("notas.csv","r") as f:
                            linea = ''
                            for i in range(ind+1):
                                linea = f.readline()
                            conn.sendall(linea.encode())
                    elif mensaje[0] == 'nota':
                        linea = mensaje[1]
                        with open("promedio.csv","w") as f:
                            f.write(f"{linea}\n")
                else:
                    print(f"no hay mas datos de {client_adress[0]}:{client_adress[1]}")
                    break
        except ConnectionError:
            print(f"Cliente {client_adress[0]}:{client_adress[1]} desconectado abruptamente")
        finally:
            conn.close()
            print(f"Conexion con {client_adress[0]:}:{client_adress[1]} cerrada") 
                    
 
