import random


if __name__ == '__main__':
    with open("notas.csv", "w+", encoding = 'utf-8') as f:
        cod_inicio = 20230001
        f.write("codigo")
        for i in range(14):
            f.write(f",l{i}")
        f.write(f",e1,e2\n")

        for i in range(200):
            f.write(f"{cod_inicio + i}")
            for i in range(16):
                f.write(f",{random.randrange(0, 20)}")
            f.write('\n')

