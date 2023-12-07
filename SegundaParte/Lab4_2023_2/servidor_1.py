import socket
import math
import time


SOCK_BUFFER = 1024

R = 6371

def convierte_radianes(grados) -> float:
    return grados * math.pi/180

def calculaDistancia(latitud1, longitud1, latitud2, longitud2) -> float:
    latitud1_rad = convierte_radianes(latitud1)
    longitud1_rad = convierte_radianes(longitud1)
    latitud2_rad = convierte_radianes(latitud2)
    longitud2_rad = convierte_radianes(longitud2)

    difLat = latitud2_rad - latitud1_rad
    difLong = longitud2_rad - longitud1_rad

    a = pow(math.sin(difLat/2), 2) + math.cos(latitud1_rad)*math.cos(latitud2_rad)*pow(math.sin(difLong/2),2)
    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    return R*c


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    print("Empezando a escuchar clientes...")
    sock.listen(1)

    while True:
        conn, client_address = sock.accept()
        print(f"Cliente conectado desde {client_address[0]}:{client_address[1]}")

        try:
            while True:
                data = conn.recv(SOCK_BUFFER)
                if data:
                    ini_atencion = time.perf_counter()
                    data_str = data.decode()
                    N = int(data_str.split(',')[0])
                    ciudad = data_str.split(',')[1]
                    latitud = []
                    longitud = []
                    distancia = []
                    ciudades = []
                    
                    ini = time.perf_counter()
                    with open("coordenadas.csv", "r") as f:
                        f.readline()
                        while True:
                            linea = f.readline()
                            if not linea:
                                break
                            datos_ciudad = linea.split(',')
                            if(datos_ciudad[0]==ciudad):
                                latitud1 = float(datos_ciudad[1])
                                longitud1 = float(datos_ciudad[2])
                            else:
                                ciudades.append(datos_ciudad[0])
                                latitud.append(float(datos_ciudad[1]))
                                longitud.append(float(datos_ciudad[2]))
                    fin = time.perf_counter()
                    for i in range(len(latitud)):
                        distancia.append(calculaDistancia(latitud1, longitud1, latitud[i],longitud[i]))
                    
                    msg = "Ciudades,Distancia\n"
                    for i in range(N):
                        minpos = distancia.index(min(distancia))
                        msg += f"{ciudades[minpos]},{distancia[minpos]}\n"
                        del ciudades[minpos]
                        del distancia[minpos]
                    conn.sendall(msg.encode())
                    fin_atencion= time.perf_counter()
                else:
                    print(f"no hay mas datos de {client_address[0]}:{client_address[1]}")
                    print(f"El tiempo de lectura del archivo es de {fin-ini} segundos")
                    print(f"El tiempo de atención del cliente es de {fin_atencion-ini_atencion} segundos")
                    break
        except ConnectionResetError:
            print(f"Cliente {client_address[0]}:{client_address[1]} desconectado abruptamente")
        finally:
            conn.close()
            print(f"Conexion con {client_address[0]}:{client_address[1]} cerrada")