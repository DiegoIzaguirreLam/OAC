import time
import requests
from threading import Thread


urls =  [
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623210949/download21.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211125/d11.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211655/d31.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212213/d4.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212607/d5.jpg' ,
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623235904/d6.jpg',
]


def descarga(url) -> bool:
    response = requests.get(url)

    if response.status_code  != 200:
        return False
    
    with open(f"./images/{url.split("/")[-1]}", "wb") as file:
        file.write(response.content)
    return True


if __name__ == '__main__':
    threads = []
    inicio = time.perf_counter()
    for url in urls:
        print(f"Descargando {url}")
        t1 = Thread(target = descarga, args = (url,))
        threads.append(t1)
        t1.start()
    for t in threads:
        t.join() 
    fin = time.perf_counter()
    print(f"Tiempo de ejecución multihilo: {fin-inicio} segundos")
