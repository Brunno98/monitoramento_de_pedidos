import os


def get_database_url():
    return os.getenv("DATABASE_URL", "postgresql://postgres:mypassword@localhost:5432/postgres")
