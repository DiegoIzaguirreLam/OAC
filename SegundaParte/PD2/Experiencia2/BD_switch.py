
import socket

host = 'localhost'
port = 5005

file_name = 'transacciones-2023.txt'
#crea el socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#asigna el socket a un host y puerto
client_socket.connect((host, port))
#envia el nombre del archivo (a crear, para que sea el mismo que el copiado)
client_socket.send(file_name.encode())

with open(file_name, 'rb') as f:
    while True:
        data = f.read(1024) #lee la linea del archivo de transacciones
        if not data:
            break
        client_socket.send(data) #envia la data al servidor

print(f"Archivo '{file_name}' enviado al servidor")

client_socket.close()



