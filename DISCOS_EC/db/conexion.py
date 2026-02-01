import psycopg2
from psycopg2.extras import RealDictCursor

def get_conexion():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="discos_ec",
        user="postgres",
        password="admin",
        cursor_factory=RealDictCursor
    )