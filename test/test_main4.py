
def test():
    palabra = "banana"
    letra = "a"
    resultado = palabra.count(letra)
    assert resultado == 3
    palabra = "banana"
    letra = "f"
    resultado = palabra.count(letra)
    assert resultado == 0
    palabra = ""
    letra = "a"
    resultado = palabra.count(letra)
    assert resultado == 0
