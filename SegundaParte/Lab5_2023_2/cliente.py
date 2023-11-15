import socket
import time

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # definicion de socket familia de socket , tipo de socket a recibir
    server_adress = ('localhost',5000)

    print(f"Conectando a servidor {server_adress[0]}:{server_adress[1]}")
    t_lectura = 0
    t_envio = 0
    inicio = time.perf_counter()
    sock.connect(server_adress)

    try:
        with open("big_file.txt","r") as f:
            while True:
                ini_r = time.perf_counter()
                msg = f.read(SOCK_BUFFER)
                fin_r = time.perf_counter()
                t_lectura += fin_r - ini_r
                if msg:
                    ini_e = time.perf_counter()
                    sock.sendall(msg.encode()) # algunos valores especiales dependen del tipo de codificación, entonces se tiene que
                                                # codificar en un formato antes de enviarlo (encoding)
                    fin_e = time.perf_counter()
                    t_envio += fin_e - ini_e
                else:
                    break
        
    finally:
        #print(f"Cerrando socket")
        socket.close
        fin = time.perf_counter()
        print(f"el tiempo de lectura es de {t_lectura} segundos")
        print(f"el tiempo de envio es de {t_envio} segundos")



