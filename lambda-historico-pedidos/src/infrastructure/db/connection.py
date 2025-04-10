from psycopg_pool import ConnectionPool
from infrastructure.settings import get_database_url

# Criando o pool uma vez só
db_pool = ConnectionPool(conninfo=get_database_url())


def get_connection():
    return db_pool.getconn()
