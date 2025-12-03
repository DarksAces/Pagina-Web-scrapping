import requests
from bs4 import BeautifulSoup
import pandas as pd

# Lista de URLs a procesar
urls_a_raspar = [
    'https://example.com',
    'https://www.python.org',
    'https://www.google.com'
]

def extraer_datos(url):
    """Extrae el título de la página y devuelve un diccionario."""
    try:
        # Petición a la URL
        respuesta = requests.get(url)
        respuesta.raise_for_status() # Lanza un error para códigos 4xx/5xx

        # Analizar el HTML
        sopa = BeautifulSoup(respuesta.text, 'html.parser')

        # Extraer el título de la página
        if sopa.find('title'):
            titulo = sopa.find('title').get_text()
        else:
            titulo = 'SIN TÍTULO'

        # Almacenar el resultado como un diccionario
        return {'url': url, 'titulo': titulo}

    except Exception as e:
        print(f"Error al raspar {url}: {e}")
        return {'url': url, 'titulo': 'ERROR DE EXTRACCIÓN'}

def ejecutar_scraping():
    print("Iniciando extracción...")
    datos_locales = []
    for url in urls_a_raspar:
        print(f"Procesando: {url}")
        resultado = extraer_datos(url)
        datos_locales.append(resultado)

    print("Extracción completa. Datos recolectados:")

    # Convertir la lista de diccionarios a un DataFrame de Pandas
    df = pd.DataFrame(datos_locales)

    # Exportar los resultados a un archivo CSV
    # ESTO ES CRUCIAL: El script de Actions subirá este archivo actualizado.
    df.to_csv('resultados_scrapping.csv', index=False, encoding='utf-8')
    print("\nDatos exportados a 'resultados_scrapping.csv'")
    return datos_locales

# Asegura que el scraping se ejecute automáticamente cuando GitHub Actions llama al script
if __name__ == "__main__":
    ejecutar_scraping()