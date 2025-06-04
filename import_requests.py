import re
import urllib.request
from collections import namedtuple


SimpleResponse = namedtuple('SimpleResponse', ['status_code', 'content'])


def funcion_para_conectar(url: str) -> SimpleResponse:
    """Realiza una solicitud HTTP GET y devuelve un objeto similar a Response."""
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        content = resp.read()
        status_code = resp.getcode()
    return SimpleResponse(status_code, content)


def funcion_para_extraer_enlaces(url: str):
    """Extrae todos los enlaces de la página indicada."""
    respuesta = funcion_para_conectar(url)
    html = respuesta.content.decode('utf-8', errors='ignore')
    enlaces = re.findall(r'href=["\']?([^"\' >]+)', html)
    return enlaces


def funcion_analisis_sentimiento(texto: str):
    """Realiza un análisis de sentimiento muy básico sobre el texto."""
    palabras = re.findall(r'\w+', texto.lower())
    positivos = {'bueno', 'positiva', 'ganancia', 'sube', 'bullish'}
    negativos = {'malo', 'negativa', 'caida', 'baja', 'bearish'}
    if not palabras:
        return namedtuple('Sentiment', ['polarity', 'subjectivity'])(0, 0)
    score = sum(1 for p in palabras if p in positivos) - sum(1 for n in palabras if n in negativos)
    total_relacionadas = sum(1 for p in palabras if p in positivos or p in negativos)
    polarity = score / len(palabras)
    subjectivity = total_relacionadas / len(palabras)
    return namedtuple('Sentiment', ['polarity', 'subjectivity'])(polarity, subjectivity)


if __name__ == "__main__":
    resp = funcion_para_conectar("https://www.coindesk.com")
    print(resp.status_code, len(resp.content))
    print(funcion_para_extraer_enlaces("https://www.coindesk.com")[:5])
    print(funcion_analisis_sentimiento("Ejemplo positivo de texto bullish"))
