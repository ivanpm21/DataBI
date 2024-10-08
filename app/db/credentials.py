import os

from db.db import DBCredentials


# Get credentials from env variables
def get_credentials() -> DBCredentials:
    
    return DBCredentials(
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        db=os.getenv('POSTGRES_DB'),
        host=os.getenv('POSTGRES_HOST'),
        port=int(os.getenv('POSTGRES_PORT'))
    )