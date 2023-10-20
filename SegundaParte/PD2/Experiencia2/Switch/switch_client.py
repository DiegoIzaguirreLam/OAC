import socket


host_A = 'localhost'
port_A = 6005

host_B = 'localhost'
port_B = 7005

file_name = 'transacciones-2023.txt'

auth_codes = ['501001', '207002']

file_name_A = 'transacciones-2023_autA.txt'
file_name_B = 'transacciones-2023_autB.txt'

file_A = open(file_name_A, 'w')
file_B = open(file_name_B, 'w')

with open(file_name, 'r') as f: # en esta parte, se lee la data que ya tiene y la separa en dos archivos (locales)
    data = f.read()
    blocks = data.split('\n*****\n') #separa la data por bloques

    for block in blocks:
        auth_code = block[-7:-1]
        if auth_code == auth_codes[0]:
            file_A.write(block)
            file_A.write('\n*****\n')
        else:
            file_B.write(block)
            file_B.write('\n*****\n')
        '''rows = []
        rows = block.split('\n')

        n_rows = len(rows)
        i = 0
        for row in rows:
            row_items = row.split(' --- ')
            if i==(n_rows-1):
                auth_code = row_items[2][5:11]
                if auth_code == auth_codes[0]:
                    file_A.write(block)
                    file_A.write('\n*****\n')
                elif auth_code == auth_codes[1]:
                    file_B.write(block)
                    file_B.write('\n*****\n')
            i = i+1'''
    f.close()

file_A.close()
file_B.close()

# a continuacion, esta parte es para enviar los archivos que ya se tienen por separado (A y B) a los respectivos clientes
SM_socket_01 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SM_socket_01.connect((host_A, port_A))
SM_socket_01.send(file_name_A.encode())


with open(file_name_A, 'rb') as f: #envia cada linea de texto del archivo recientemente creado al autorizador A
    while True:
        data = f.read(1024)
        if not data:
            break
        SM_socket_01.send(data)

print(f"Archivo '{file_name_A}' enviado al Autorizador A")


SM_socket_02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SM_socket_02.connect((host_B, port_B))
SM_socket_02.send(file_name_B.encode())


with open(file_name_B, 'rb') as f: #envia cada linea de texto del archivo recientemente creado al autorizador B
    while True:
        data = f.read(1024)
        if not data:
            break
        SM_socket_02.send(data)

print(f"Archivo '{file_name_B}' enviado al Autorizador B")
