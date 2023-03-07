import unittest
from misfunciones import inverso,suma_cuadrados,eliminar_repetidos,es_primo

class TestInverso(unittest.TestCase):
    def test_inverso_entre_enteros(self):
        self.assertEqual(inverso(2), 0.5)
        self.assertEqual(inverso(5), 0.2)
         
    def test_inverso_de_cero(self):
        with self.assertRaises(ValueError):
            inverso(0)
            
class TestSumaCuadrados(unittest.TestCase):
    def test_suma_cuadrados(self):
        lista = [1, 2, 3, 4]
        suma = suma_cuadrados(lista)
        self.assertEqual(suma, 30)

class TestEliminarRepetidos(unittest.TestCase):
    def test_eliminar_repetidos(self):
        lista = [1, 4, 2, 3, 1, 2, 3, 2, 4, 3]
        resultado = eliminar_repetidos(lista)
        self.assertCountEqual(resultado, [1, 2, 3, 4])      
        
class TestEsPrimo(unittest.TestCase):
    def test_es_primo_numero_negativo(self):
        self.assertFalse(es_primo(-5))

    def test_es_primo_numero_cero(self):
        self.assertFalse(es_primo(0))

            
if __name__ == "__main__":
    unittest.main()




