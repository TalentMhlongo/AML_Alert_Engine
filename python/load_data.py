import pandas as pd
from sqlalchemy import create_engine
from config import (
    DATA_SOURCE,
    CUSTOMERS_FILE,
    DEPOSITS_FILE,
    DB2_HOST,
    DB2_PORT,
    DB2_NAME,
    DB2_USER,
    DB2_PASSWORD,
    CUSTOMERS_TABLE,
    DEPOSITS_TABLE,
)


 

def load_from_csv():
    customers = pd.read_csv(CUSTOMERS_FILE)
    deposits = pd.read_csv(DEPOSITS_FILE)
    return customers, deposits

def get_db_engine():
    connection_string = (
        f"ibm_db_sa://{DB2_USER}:{DB2_PASSWORD}"
        f"@{DB2_HOST}:{DB2_PORT}/{DB2_NAME}"
    )
    return create_engine(connection_string)

def load_from_db():
    engine = get_db_engine()
    customers = pd.read_sql(f"SELECT * FROM {CUSTOMERS_TABLE}", engine)
    deposits = pd.read_sql(f"SELECT * FROM {DEPOSITS_TABLE}", engine)
    return customers, deposits

def load_all_data():
    if DATA_SOURCE.lower() == "db":
        return load_from_db()
    return load_from_csv()
