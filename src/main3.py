
def cuenta(cadena, letra):
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador

if __name__ == '__main__':
    palabra = "platano"

    conteo = cuenta("palabra","a")

    print(conteo)