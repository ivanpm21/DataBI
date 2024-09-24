import os
from dotenv import load_dotenv

from db.db import DBCredentials

load_dotenv('.env', override=True)


def get_credentials() -> DBCredentials:
    
    return DBCredentials(
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        db=os.getenv('POSTGRES_DB'),
        host=os.getenv('POSTGRES_HOST'),
        port=int(os.getenv('POSTGRES_PORT'))
    )