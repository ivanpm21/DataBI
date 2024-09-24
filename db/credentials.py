import os

from db.db import DBCredentials

def get_credentials() -> DBCredentials:
    
    return DBCredentials(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT'))
    )