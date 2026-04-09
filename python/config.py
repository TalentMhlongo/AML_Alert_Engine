import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed")

CUSTOMERS_FILE = os.path.join(RAW_DATA_PATH, "customers.csv")
DEPOSITS_FILE = os.path.join(RAW_DATA_PATH, "deposits.csv")








DATA_SOURCE = os.getenv("DATA_SOURCE", "csv")  # csv or db

DB2_HOST = os.getenv("DB2_HOST")
DB2_PORT = os.getenv("DB2_PORT")
DB2_NAME = os.getenv("DB2_NAME")
DB2_USER = os.getenv("DB2_USER")
DB2_PASSWORD = os.getenv("DB2_PASSWORD")

CUSTOMERS_TABLE = "HWB_CUSTOMERS"
DEPOSITS_TABLE = "HWB_DEPOSITS"

THRESHOLD = 50000
NEAR_THRESHOLD_MIN = 40000
NEAR_THRESHOLD_MAX = 49999
STRUCTURING_COUNT = 3
HIGH_FREQUENCY_COUNT = 5
