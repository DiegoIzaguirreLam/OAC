import socket
#cliente -> servidor (BD -> switch)
host = 'localhost'
port = 5005
#crea un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#enlaza el socket al host y puerto
server_socket.bind((host,port))
#puede escuchar hasta 5 conexiones entrantes 'en cola'
server_socket.listen(5)

print(f"Servidor de transferencia de archivos escuchando en {host}:{port}")

#espera a que un cliente se conecte
client_socket, client_adress = server_socket.accept()
print(f"Conexión entrante desde {client_adress}")

#recibe el nombre del archivo en la carpeta
file_name = client_socket.recv(22).decode() #22: nro. de caracteres de 'transacciones-2023.txt'

with open(file_name, 'wb') as f:
    while True:
        data = client_socket.recv(1024) #recibe la informacion del cliente
        if not data:
            break
        f.write(data) #copia la informacion recibida al archivo creaedo

print(f"Archivo '{file_name}' enviado al servidor")

client_socket.close()
server_socket.close()
