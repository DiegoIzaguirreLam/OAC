
import socket

host_B = 'localhost'
port_B = 7005


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host_B, port_B))

server_socket.listen(1)

print(f"Servidor de transferencia de archivos escuchando en {host_B}:{port_B}")


client_socket, client_adress = server_socket.accept()
print(f"Conexión entrante desde {client_adress}")

file_name = client_socket.recv(27).decode()

with open(file_name, 'wb') as f:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        f.write(data)

print(f"Archivo '{file_name}' enviado al servidor")

client_socket.close()
server_socket.close()
