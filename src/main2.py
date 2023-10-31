
# Dado que fruta es una variable de tipo cadena, ¿qué significa fruta[:]?
def string_comlpeto(string):
    return string[:]

if __name__ == '__main__':
    
    fruta = "manzana"

    stringlineal = string_comlpeto(fruta)
    
    print(stringlineal)

    # Es un Slice que contiene toda el String