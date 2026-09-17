import pandas as pd

BASE_URL = f'https://data.cityofchicago.org/resource/igwz-8jzy.json'
comunity_areas_filename :str = 'community_areas.csv'
raw_data_path :str = './data/raw/'
# Guardar datos en un dataframe
df_full = pd.read_json(BASE_URL)
# Conservar solo el id y nombre
df = df_full[['area_numbe', 'community']]
# Agregar el caso para datos faltantes, por ejemplo porque el viaje del taxi va fuera de la ciudad
df.loc[0] = [None, 'N/A']
# Convertir a Int64 para admitir nulos
df['area_numbe'] = df['area_numbe'].astype("Int64")
# Exportar resultados a data/raw
df.to_csv(raw_data_path + comunity_areas_filename, index=False)