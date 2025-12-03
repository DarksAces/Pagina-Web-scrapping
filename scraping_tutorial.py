import requests
from bs4 import BeautifulSoup
import pandas as pd

# Lista de URLs a procesar
urls_a_raspar = [
    'https://example.com',
    'https://www.python.org',
    'https://www.google.com'
]

# Creamos una lista vacía para almacenar los datos extraídos
datos_extraidos = []

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

# Iterar sobre la lista de URLs y llenar la lista 'datos_extraidos'
print("Iniciando extracción...")
for url in urls_a_raspar:
    print(f"Procesando: {url}")
    resultado = extraer_datos(url)
    datos_extraidos.append(resultado)

print("Extracción completa. Datos recolectados:")
print(datos_extraidos)

# Convertir la lista de diccionarios a un DataFrame de Pandas
df = pd.DataFrame(datos_extraidos)

# Mostrar el DataFrame
print("\nDataFrame de Pandas:")
print(df)

# Ejemplo de análisis o manipulación con Pandas:
# Contar cuántas filas se extrajeron sin errores
filas_exitosas = df[df['titulo'] != 'ERROR DE EXTRACCIÓN'].shape[0]

print(f"\nNúmero de filas extraídas con éxito: {filas_exitosas}")

# Exportar los resultados a un archivo CSV
df.to_csv('resultados_scrapping.csv', index=False, encoding='utf-8')
print("\nDatos exportados a 'resultados_scrapping.csv'")
