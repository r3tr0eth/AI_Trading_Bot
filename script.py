# URL base para cada sitio web de noticias
base_url_cointelegraph = "https://es.cointelegraph.com"
base_url_coindesk = "https://www.coindesk.com/es"
base_url_bloomberg = "https://www.bloomberg.com"

# Rutas relativas extraídas (sustituye con las tuyas)
rutas_relativas = [
    "/markets/2023/12/20/bitcoin-could-reach-160k-in-2024-on-the-back-of-halving-spot-etf-hype-analysts/",
    # ... más rutas relativas
]

# Concatenar la URL base con las rutas relativas
urls_completas_cointelegraph = [base_url_cointelegraph + ruta for ruta in rutas_relativas if ruta.startswith("/markets")]
urls_completas_coindesk = [base_url_coindesk + ruta for ruta in rutas_relativas if ruta.startswith("/es/markets")]
urls_completas_bloomberg = [base_url_bloomberg + ruta for ruta in rutas_relativas if ruta.startswith("/crypto")]

# Imprimir las URLs completas
print("URLs completas de CoinTelegraph:")
for url in urls_completas_cointelegraph:
    print(url)

print("\nURLs completas de CoinDesk:")
for url in urls_completas_coindesk:
    print(url)

print("\nURLs completas de Bloomberg:")
for url in urls_completas_bloomberg:
    print(url)