import psycopg
from psycopg.rows import dict_row


DB_CONFIG = {
    "host": "localhost",
    "dbname": "postgres",
    "user": "postgres",
    "password": "admin",
    "port": "5432",
    "options": "-c search_path=ispc,public"
}



def get_connection():
    return psycopg.connect(**DB_CONFIG, row_factory=dict_row)