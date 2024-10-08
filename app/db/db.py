from contextlib import contextmanager
from dataclasses import dataclass

import psycopg

# Class for storing credentials
@dataclass
class DBCredentials:
    db: str
    user: str
    password: str
    host: str
    port: int

# Class for database connection with conext manager 
class DatabaseConnection:
    def __init__(self, cred: DBCredentials) -> None:
        
        self.conn_url = (
            f'postgresql://{cred.user}:{cred.password}@{cred.host}:{cred.port}/{cred.db}'
        )

    @contextmanager
    def df_cursor(self):
        self.conection = psycopg.connect(self.conn_url)
        self.conection.autocommit = True
        self.cursor = self.conection.cursor()

        try:
            yield self.cursor
        finally:
            self.cursor.close()
            self.conection.close()
