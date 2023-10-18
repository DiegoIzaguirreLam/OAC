

if __name__ == '__main__':
    frase = "Hola OAC 2023-2"

    with open("archivo.txt", "w+", encoding="utf-8") as f: # w es de escritura y el + es para sobreescribir el archivo. si no se pone el +, se concatena
        f.write(frase)
    



