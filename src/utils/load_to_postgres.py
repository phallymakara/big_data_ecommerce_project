import os
import sys
import pandas as pd
from sqlalchemy import create_engine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from config import get_sqlalchemy_url
  # config file

csv_directory = 'data/raw'  # Folder containing CSV files

engine = create_engine(get_sqlalchemy_url())

connection_url = get_sqlalchemy_url()
print("Connection URL:", connection_url)
engine = create_engine(connection_url)


for filename in sorted(os.listdir(csv_directory)):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_directory, filename)
        # Use filename without extension as table name
        table_name = os.path.splitext(filename)[0]

        print(f'Processing file: {file_path} -> Table: {table_name}')
        
        df = pd.read_csv(file_path)
        
        # Create or replace table for each CSV
        df.to_sql(table_name, engine, if_exists='replace', index=False)

print('✅ All CSV files uploaded with their own table names!')
