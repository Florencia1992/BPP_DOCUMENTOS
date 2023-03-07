
def inverso(num):
    if num == 0:
        raise ValueError("No se puede calcular el inverso de cero")
    return 1 / num

def suma_cuadrados(lista):
    return sum([num**2 for num in lista])

def eliminar_repetidos(lista):
    return list(set(lista))

def contar_vocales(cadena):
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    for letra in cadena.lower():
        if letra in vocales:
            contador += 1
    return contador

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True