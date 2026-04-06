import pandas as pd
from sqlalchemy import create_engine
from config import (
    DB2_HOST,
    DB2_PORT,
    DB2_NAME,
    DB2_USER,
    DB2_PASSWORD,
    CUSTOMERS_TABLE,
    DEPOSITS_TABLE
)


def get_engine():
    connection_string = (
        f"ibm_db_sa://{DB2_USER}:{DB2_PASSWORD}"
        f"@{DB2_HOST}:{DB2_PORT}/{DB2_NAME}"
    )
    engine = create_engine(connection_string)
    return engine


def load_customers():
    engine = get_engine()
    query = f"SELECT * FROM {CUSTOMERS_TABLE}"
    df = pd.read_sql(query, engine)
    return df


def load_deposits():
    engine = get_engine()
    query = f"SELECT * FROM {DEPOSITS_TABLE}"
    df = pd.read_sql(query, engine)
    return df


def load_all_data():
    customers = load_customers()
    deposits = load_deposits()
    return customers, deposits
