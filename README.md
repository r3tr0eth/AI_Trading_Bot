# Crypto Sentiment Trading Bot
## Descripción
Este bot de trading automatizado está diseñado para operar en el mercado de criptomonedas utilizando una estrategia de Dollar Cost Averaging (DCA) combinada con análisis de sentimiento del mercado. El bot recopila noticias de criptomonedas de fuentes confiables como CoinDesk, analiza el sentimiento de estas noticias utilizando BeautifulSoup para el web scraping y TextBlob para el análisis de sentimientos. Basándose en este análisis, el bot toma decisiones de trading, considerando un mercado bajista (bearish) cuando la polaridad es negativa y la subjetividad es alta, y un mercado alcista (bullish) en el caso opuesto.

## Características
- Recopilación de Noticias: Utiliza BeautifulSoup para hacer scraping de noticias de criptomonedas en tiempo real.
- Análisis de Sentimiento: Emplea TextBlob para analizar el tono de las noticias recopiladas.
- Estrategia de Trading: Implementa una estrategia basada en DCA, ajustada según el análisis de sentimiento del mercado.

## Criterios de Trading:
- umbral_polaridad_bearish = 0: Polaridad por debajo de 0 se considera bearish.
- umbral_subjetividad_alta = 0.5: Subjetividad por encima de 0.5 se considera alta.

## Requisitos
```Python 3.6 o superior
Bibliotecas: BeautifulSoup, TextBlob, (otras bibliotecas que se usen)
```
## Instalación
Para instalar este bot, clona este repositorio y luego instala las dependencias:
```
bash
Copy code
git clone [URL del repositorio]
cd trading-bot
pip install -r requirements.txt
````

## Uso
Para ejecutar el bot, navega a la carpeta del proyecto y ejecuta:
```
bash
Copy code
python src/script.py
```

## Contribuciones
Las contribuciones son bienvenidas. Si tienes alguna mejora o corrección, por favor abre un pull request.

## Licencia
Este proyecto está bajo la licencia MIT License. Consulta el archivo LICENSE para más detalles.

# Contacto

Para cualquier consulta o sugerencia, no dudes en contactarme a través de r3tr0_13@proton.me