from bs4 import BeautifulSoup
import pandas as pd

def process_html(html: str, filename: str):

    # Se podría hacer directamente con read_html pero demostraremos como se hace con bs4
    # tables = pd.read_html(html)
    # df = tables[0]  # tomar la primera tabla encontrada

    with open("data/external/"+html, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Convertir a árbol
    soup = BeautifulSoup(html_content, 'lxml')

    # Encontrar la parte que contiene la tabla
    table = soup.find('table', attrs={"id": "weather_records"})

    # Extraer los nombres de las columnas
    col_names = []
    for row in table.find_all('th'):
        col_names.append(row.text)
        
    # Extraer el contenido de la tabla por filas
    rows = []  
    for row in table.find_all('tr'):
        if not row.find_all('th'):
            # Necesitamos esta condición para ignorar la primera fila de la tabla, con encabezados
            rows.append([element.text for element in row.find_all('td')])

    # Crear el DataFrame y exportarlo
    records = pd.DataFrame(rows, columns=col_names)
    records.to_csv("data/processed/"+filename, index=False)


if __name__ == "__main__":
    process_html('weather.html','weather.csv')