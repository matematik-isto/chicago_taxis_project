import requests
from pathlib import Path

def fetch_html_and_save(url: str, filename: str):
    response = requests.get(url)
    response.raise_for_status()
    script_dir = Path(__file__).resolve().parent
# Subir un nivel para llegar a la raíz del proyecto y luego a datos/
    project_root = script_dir.parent
    raw_path = project_root/"data"/"raw"
    raw_path.mkdir(parents=True, exist_ok=True)

    output_file = raw_path / filename
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"HTML guardado en {output_file}")

if __name__ == "__main__":
    url_weather = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'
    filename_weather = "weather.html"
    fetch_html_and_save(url_weather, filename_weather)  