import unittest
from apoyo_desafio import Foto
from error import DimensionError

'''
    Estoy probando un generador de tests y leyendo un poco acerca de testing en Python.
'''

class TestFoto(unittest.TestCase):
    def test_validar_dimension(self):
        # Test case where dimension is within the allowed range
        self.assertIsNone(Foto.validar_dimension(2000))

        # Test case where dimension exceeds the allowed range
        with self.assertRaises(DimensionError):
            Foto.validar_dimension(3000)

    def test_ancho(self):
        foto = Foto(1000, 800, "ruta")

        # Test case where ancho is within the allowed range
        foto.ancho = 1500
        self.assertEqual(foto.ancho, 1500)

        # Test case where ancho exceeds the allowed range
        with self.assertRaises(DimensionError):
            foto.ancho = 3000

    def test_alto(self):
        foto = Foto(1000, 800, "ruta")

        # Test case where alto is within the allowed range
        foto.alto = 1200
        self.assertEqual(foto.alto, 1200)

        # Test case where alto exceeds the allowed range
        with self.assertRaises(DimensionError):
            foto.alto = 3000

if __name__ == '__main__':
    unittest.main()