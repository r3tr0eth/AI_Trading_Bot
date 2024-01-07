import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Definición de las URLs de los sitios de noticias
urls = [
    "https://www.coindesk.com/es/"
]

enlaces_noticias = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra y guarda los enlaces a las noticias. Ajusta este código según la estructura del sitio.
    for enlace in soup.find_all("a"):  # Ajusta el selector según sea necesario
        titulo = enlace.get_text().strip()
        if any(palabra in titulo.lower() for palabra in ["crypto", "ethereum", "bitcoin", "solana"]):
            enlaces_noticias.append(enlace['href'])  # Asegúrate de que 'href' es el atributo correcto

    if len(enlaces_noticias) >= 30:
        break

# URL base para cada sitio web de noticias
base_url_coindesk = "https://www.coindesk.com"

# Concatenar la URL base con las rutas relativas
urls_completas_coindesk = [base_url_coindesk + ruta for ruta in enlaces_noticias if ruta.startswith("/markets") or ruta.startswith("/tech") or ruta.startswith("/policy")]

# Diccionario para almacenar los resultados

cuerpos_noticias = []

for url in urls_completas_coindesk:
    response = requests.get(url)
    # Asegúrate de manejar excepciones y posibles errores de respuesta aquí
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Aquí necesitas encontrar el selector correcto para el cuerpo de las noticias
    # Este es un selector genérico, tendrás que ajustarlo según el sitio web
    cuerpo_noticia = soup.find('div', class_='containerstyles__StyledContainer-sc-292snj-0 KqMZq article-bodystyles__StyledWrapper-sc-5qmdhl-0 fEKnok').get_text()
    cuerpos_noticias.append(cuerpo_noticia)

print(cuerpos_noticias)
