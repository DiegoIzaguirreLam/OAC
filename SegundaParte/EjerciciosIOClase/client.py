import socket

SOCK_BUFFER = 1024

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_adress = ('localhost', 5001)

    print(f"Conectando a servidor {server_adress[0]}:{server_adress[1]}")

    client_socket.connect(server_adress)
    try:
        msg = "codigo:20230009"
        client_socket.send(msg.encode())
        raw = client_socket.recv(SOCK_BUFFER)
        data = raw.decode()
        print(f"Codigo Recibido: {data}",end='')
        notas_str = data.split(',')
        codigo = notas_str[0]
        notas_str = notas_str[1:]
        notas_int = [int(nota) for nota in notas_str]
        promedio = sum(notas_int)/len(notas_int)
        msg = f"nota:{codigo},{round(promedio, 2)}"
        client_socket.send(msg.encode())
        print(f"Enviado: {msg}")
    finally:
        print(f"Cerrando socket")
        client_socket.close()

#cliente guarda promedio y se lo envia al servidor, luego el servidor lo guarda en un archivo promedio.csv:
#se envia con el prefijo "nota:"
#codigo, promedio 
