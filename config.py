from dotenv import load_dotenv
import os

load_dotenv()

def get_sqlalchemy_url():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    # Debugging: print the loaded variables
    print("Loaded from .env:")
    print(f"User: {user}, Password: {password}, Host: {host}, Port: {port}, DB: {database}")
    
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

