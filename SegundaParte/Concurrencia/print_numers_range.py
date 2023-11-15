from threading import Thread


def print_pares(a, b):
    for i in range(a, b):
        if i%2==0:
            print(i)

def print_impares(a, b):
    for i in range(a, b):
        if i%2!=0:
            print(i)

if __name__ == '__main__':
    a = 30
    b = 50
    t1 = Thread(target = print_pares, args = (a,b,))
    t2 = Thread(target = print_impares, args = (a,b,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

