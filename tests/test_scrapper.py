import unittest
from import_requests import (funcion_para_conectar, funcion_para_extraer_enlaces, funcion_analisis_sentimiento)

class TestScraperNoticias(unittest.TestCase):

    def test_conexion_url(self):
        """ Verifica si la conexión a la URL es exitosa """
        url = "https://www.coindesk.com"
        respuesta = funcion_para_conectar(url)
        self.assertEqual(respuesta.status_code, 200)

    def test_extraccion_enlaces(self):
        """ Verifica si los enlaces se extraen correctamente """
        url = "https://www.coindesk.com"
        enlaces = funcion_para_extraer_enlaces(url)
        self.assertGreater(len(enlaces), 0)  # Asegura que se extraiga al menos un enlace

    def test_analisis_sentimiento(self):
        """ Verifica el funcionamiento del análisis de sentimiento """
        texto = "Este es un ejemplo de noticia positiva sobre criptomonedas."
        sentimiento = funcion_analisis_sentimiento(texto)
        self.assertIsNotNone(sentimiento)  # Comprueba que se devuelva algún resultado

if __name__ == '__main__':
    unittest.main()