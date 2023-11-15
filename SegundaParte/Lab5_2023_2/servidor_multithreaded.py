import socket
import time
from threading import Thread
SOCK_BUFFER = 1024

t_recepcion = 0
t_escritura = 0

def data_recv(data, filename):
    global t_escritura

    with open(filename, 'a') as f:
        ini_e = time.perf_counter()
        f.write(data.decode())
        fin_e = time.perf_counter()
        t_escritura += fin_e-ini_e


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_adress = ('localhost', 5000)

    print(f"Iniciando servidor en {server_adress[0]}:{server_adress[1]}")

    sock.bind(server_adress)

    print("Empezando a escuchar clientes...")
    sock.listen(1) #es como el numero de clientes que pueden estar "en cola" esperando para ser atendidos. 
                    # en este caso, mientras que se atiene 1, 1 está en la cola, entonces un tercer cliente no será atendido
    ind = 0
    while True:
        conn, client_adress = sock.accept() #esto espera una conexion, bloquea el código hasta que haya una conexión. cuando haya una conexión,
                                            #retorna 
        print(f"Cliente conectado desde: {client_adress[0]}:{client_adress[1]}")
        ini = time.perf_counter()
        try: #lo usamos para que la conexión no se caiga
            open("big_file_server.txt", "w", encoding='utf-8').close()
            while True:
                ini_r = time.perf_counter()
                data = conn.recv(SOCK_BUFFER) # se queda esperando hasta que reciba data. a veces hay un timeout, donde retorna nulo si no recibe data
                fin_r = time.perf_counter()
                if data:
                    t_recepcion += fin_r - ini_r 
                    t1 = Thread(target = data_recv, args=(data, "big_file_server.txt"))
                    t1.start()
                else:
                    print(f"no hay mas datos de {client_adress[0]}:{client_adress[1]}")
                    break
        except ConnectionError:
            print(f"Cliente {client_adress[0]}:{client_adress[1]} desconectado abruptamente")
        finally:
            conn.close()
            fin = time.perf_counter()
            print(f"Conexion con {client_adress[0]}:{client_adress[1]} cerrada")
            #print(f"el tiempo de recepcion total es de {t_recepcion} segundos")
            #print(f"el tiempo de escritura total es de {t_escritura} segundos")
            print(f"el tiempo de transaccion total es de {fin-ini} segundos")



