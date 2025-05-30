import os, logging
from pymssql import connect, Connection
from dotenv import load_dotenv


def create_connection() -> Connection | None:
    # read data from .env file
    load_dotenv()
    db_server = os.getenv('DB_SERVER')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')

    # connect to the SQL Server
    try:
        return connect(server=db_server, user=db_user, password=db_password, database=db_name)
    except Exception as e:
        logging.error(f'Error connecting to the SQL Server database: {e}')
