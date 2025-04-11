from psycopg_pool import ConnectionPool
from infrastructure.settings import get_database_url

# Criando o pool uma vez só
db_pool = ConnectionPool(
    min_size=1,
    max_size=10,
    conninfo=get_database_url())


def get_connection():
    return db_pool.connection()
