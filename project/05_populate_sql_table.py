# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 16:23:47 2025

@author: RCorrea
"""
import warnings
import pyodbc
import pandas as pd
from sqlalchemy import create_engine
warnings.filterwarnings('ignore')


# En vez de usar un .csv intermedio es posible escribir en la base de datos directamente de la lectura de la API mediante json
trips_filename :str = 'Taxi_Trips_-_2017_Nov.csv'
comunity_areas_filename :str = 'community_areas.csv'
raw_data_path :str = '../data/raw/'
driver :str = "ODBC Driver 17 for SQL Server" 
server :str = r"localhost\SQL22"  
database :str = "Chicago_taxis" 
trust :str = "yes"

connector = pyodbc.connect(
     f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection={trust};'
    )

# Crear un engine de SQLAlchemy a partir de pyodbc
engine = create_engine("mssql+pyodbc://", creator=lambda: connector)

community_df = pd.read_csv(raw_data_path+comunity_areas_filename)
community_df.to_sql('neighborhoods',con = engine, if_exists =  'replace', index= False)
'''
trips_df = pd.read_csv(raw_data_path+trips_filename)

for k in range(250):
    trips_df[k*100000:(k+1)*100000].to_sql('2017_taxi_trips_raw', con = engine, if_exists = "append", index= False)
'''
connector.close()
