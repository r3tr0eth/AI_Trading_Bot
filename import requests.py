import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# URLs de los sitios de noticias
urls = [
    "https://www.coindesk.com"
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
    cuerpo_noticia = soup.find('main', class_='sticky-article-body').get_text()
    cuerpos_noticias.append(cuerpo_noticia)

analisis_sentimiento = {}

# Inicializa las listas para almacenar valores individuales de polaridad y subjetividad
polaridades = []
subjetividades = []

# Llena el diccionario con el análisis de sentimiento y las listas con los valores individuales
for url, cuerpo in zip(urls_completas_coindesk, cuerpos_noticias):
    analisis = TextBlob(cuerpo)
    analisis_sentimiento[url] = analisis.sentiment
    polaridades.append(analisis.sentiment.polarity)
    subjetividades.append(analisis.sentiment.subjectivity)

# Calcula la suma de polaridades y subjetividades
suma_polaridad = sum(polaridades)
suma_subjetividad = sum(subjetividades)

# Guarda las sumas para uso posterior (por ejemplo, para calcular medias)
conteo_noticias = len(polaridades)  # o len(analisis_sentimiento) si prefieres
resultado_analisis = {
    'suma_polaridad': suma_polaridad,
    'suma_subjetividad': suma_subjetividad,
    'conteo_noticias': conteo_noticias
}

print(resultado_analisis)

    # Basado en el resultado anterior y las instrucciones proporcionadas, vamos a implementar la lógica de trading:

# Estrategia de trading basada en DCA y sentimiento del mercado
# Suponiendo que una polaridad negativa y alta subjetividad indican un mercado bajista (bearish)
# y una polaridad positiva y alta subjetividad indican un mercado alcista (bullish)

# Calcular la media de la polaridad y subjetividad
polaridad_media = suma_polaridad / conteo_noticias
subjetividad_media = suma_subjetividad / conteo_noticias

# Definir umbrales para polaridad y subjetividad
# Estos umbrales son arbitrarios y deben ser ajustados para reflejar tu tolerancia al riesgo y estrategia
umbral_polaridad_bearish = 0  # Polaridad por debajo de 0 se considera bearish
umbral_subjetividad_alta = 0.5  # Subjetividad por encima de 0.5 se considera alta

# Implementar la lógica de trading
if polaridad_media < 0:
    accion_trading = "Comprar"
elif polaridad_media > 0:
    accion_trading = "Vender"
else:
    accion_trading = "Mantener"

print(accion_trading, polaridad_media, subjetividad_media)
