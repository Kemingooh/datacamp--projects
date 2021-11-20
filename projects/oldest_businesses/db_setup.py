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
DDL_SQL_SCRIPT = os.path.join(
    os.path.dirname(__file__),
    'assets/ddl/createdb.sql')

DATA_CSV_BUSINESSES = os.path.join(
    os.path.dirname(__file__),
    'assets/data/businesses.csv')

DATA_CSV_AGE_CATEGORIES = os.path.join(
    os.path.dirname(__file__),
    'assets/data/categories.csv')

DATA_CSV_COUNTRIES = os.path.join(
    os.path.dirname(__file__),
    'assets/data/countries.csv')

# Attempt to run the DDLs
run_sql(DB_PARAMS, DDL_SQL_SCRIPT)

# Attempt to insert data
csv_to_table(DB_PARAMS, DATA_CSV_BUSINESSES, 'businesses', quote='"')
csv_to_table(DB_PARAMS, DATA_CSV_AGE_CATEGORIES, 'categories', quote='"')
csv_to_table(DB_PARAMS, DATA_CSV_COUNTRIES, 'countries', quote='"')
