import pytest
from misfunciones import inverso,suma_cuadrados,eliminar_repetidos,es_primo

def test_inverso_entre_enteros():
    assert inverso(2) == 0.5
    assert inverso(5) == 0.2

def test_inverso_de_cero():
    with pytest.raises(ValueError):
        inverso(0)

def test_suma_cuadrados():
    lista = [1, 2, 3, 4]
    suma = suma_cuadrados(lista)
    assert suma

def test_eliminar_repetidos():
    lista = [1, 2, 3, 2, 4, 3, 2, 3]
    resultado = eliminar_repetidos(lista)
    assert set(resultado) == {1, 2, 3, 4}

def test_es_primo_numero_negativo():
    assert es_primo(-5) == False
    
def test_es_primo_numero_cero():
    assert es_primo(0) == False
        

if __name__ == "__main__":
    pytest.main()
