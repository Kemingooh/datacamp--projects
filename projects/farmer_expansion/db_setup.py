import os
import sys

# fix python path for lib
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from lib.db import run_sql  # pylint: disable=import-error, wrong-import-position
from lib.db import csv_to_table  # pylint: disable=import-error, wrong-import-position

DB_PARAMS = {
    "host": "localhost",
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres"
}

# External fieles, relative paths to the script location!
DDL_SQL_SCRIPT = 'assets/ddl/createdb.sql'
DDL_SQL_SCRIPT = os.path.join(os.path.dirname(__file__), DDL_SQL_SCRIPT)

DATA_CSV_PURCHASES_2019 = 'assets/data/2019_purchases.csv'
DATA_CSV_PURCHASES_2019 = os.path.join(os.path.dirname(__file__), DATA_CSV_PURCHASES_2019)

DATA_CSV_PURCHASES_2020 = 'assets/data/2020_purchases.csv'
DATA_CSV_PURCHASES_2020 = os.path.join(os.path.dirname(__file__), DATA_CSV_PURCHASES_2020)

DATA_CSV_CATEGORIES = 'assets/data/categories.csv'
DATA_CSV_CATEGORIES = os.path.join(os.path.dirname(__file__), DATA_CSV_CATEGORIES)

# Attempt to run the DDLs
run_sql(DB_PARAMS, DDL_SQL_SCRIPT)

# Attempt to insert data
csv_to_table(DB_PARAMS, DATA_CSV_PURCHASES_2019, 'purchases_2019')
csv_to_table(DB_PARAMS, DATA_CSV_PURCHASES_2020, 'purchases_2020')
csv_to_table(DB_PARAMS, DATA_CSV_CATEGORIES, 'categories')
