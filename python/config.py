import os

# Load from environment variables (SAFE)
DB2_HOST = os.getenv("DB2_HOST")
DB2_PORT = os.getenv("DB2_PORT")
DB2_NAME = os.getenv("DB2_NAME")
DB2_USER = os.getenv("DB2_USER")
DB2_PASSWORD = os.getenv("DB2_PASSWORD")

# Tables
CUSTOMERS_TABLE = "HWB_CUSTOMERS"
DEPOSITS_TABLE = "HWB_DEPOSITS"

THRESHOLD = 50000
