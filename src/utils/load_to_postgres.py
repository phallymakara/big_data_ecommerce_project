# src/utils/load_to_postgres.py

from pyspark.sql import SparkSession
import os
from config import DB_CONFIG

folder_path = 'data/raw'

def load_csvs_to_postgres(folder_path, table_name_prefix="table_"):
    spark = SparkSession.builder \
        .appName("CSV to PostgreSQL") \
        .config("spark.jars", "/path/to/postgresql-42.6.0.jar") \
        .getOrCreate()

    files = sorted([f for f in os.listdir(folder_path) if f.endswith(".csv")])

    for i, filename in enumerate(files, start=1):
        full_path = os.path.join(folder_path, filename)
        df = spark.read.option("header", "true").csv(full_path)

        table_name = f"{table_name_prefix}{i}"

        df.write.jdbc(
            url=DB_CONFIG["url"],
            table=table_name,
            mode="overwrite",  # or 'append'
            properties=DB_CONFIG["properties"]
        )

        print(f"Pushed {filename} -> PostgreSQL table: {table_name}")

    spark.stop()
