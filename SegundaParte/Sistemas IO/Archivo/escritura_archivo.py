

if __name__ == '__main__':

    with open("archivo.txt", "w+", encoding = "utf-8") as f:
        cod_inicio = 20230001

        for i in range(50):
            f.write(f"{cod_inicio + i}\n")