import requests
from bs4 import BeautifulSoup

# Definición de las URLs de los sitios de noticias
urls = [
    "https://es.cointelegraph.com/",
    "https://www.coindesk.com/es/",
    "https://www.bloomberg.com/crypto"
]

noticias_bitcoin = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Aquí debes ajustar las búsquedas según la estructura de cada sitio
    # Buscando elementos que contengan noticias. Este es un ejemplo genérico.
    for elemento in soup.find_all("h2"):  # Puede ser necesario ajustar el elemento (h1, h2, p, etc.)
        if "bitcoin" in elemento.get_text().lower():
            noticias_bitcoin.append(elemento.get_text().strip())

    # Limita la cantidad de noticias si es necesario
    if len(noticias_bitcoin) >= 20:
        break

enlaces_noticias = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra y guarda los enlaces a las noticias. Ajusta este código según la estructura del sitio.
    for enlace in soup.find_all("a"):  # Ajusta el selector según sea necesario
        titulo = enlace.get_text().strip()
        if "bitcoin" in titulo.lower():
            enlaces_noticias.append(enlace['href'])  # Asegúrate de que 'href' es el atributo correcto

    if len(enlaces_noticias) >= 20:
        break

print(enlaces_noticias)
