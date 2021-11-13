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

DATA_CSV_SPONSORED_ANIMALS = 'assets/data/sponsored_pets.csv'
DATA_CSV_SPONSORED_ANIMALS = os.path.join(os.path.dirname(__file__), DATA_CSV_SPONSORED_ANIMALS)

DATA_CSV_AGE_COSTS = 'assets/data/age_costs.csv'
DATA_CSV_AGE_COSTS = os.path.join(os.path.dirname(__file__), DATA_CSV_AGE_COSTS)

DATA_CSV_LOCATION_COSTS = 'assets/data/location_costs.csv'
DATA_CSV_LOCATION_COSTS = os.path.join(os.path.dirname(__file__), DATA_CSV_LOCATION_COSTS)

DATA_CSV_SIZE_COSTS = 'assets/data/size_costs.csv'
DATA_CSV_SIZE_COSTS = os.path.join(os.path.dirname(__file__), DATA_CSV_SIZE_COSTS)

DATA_CSV_ANIMALS = 'assets/data/animal_data.csv'
DATA_CSV_ANIMALS = os.path.join(os.path.dirname(__file__), DATA_CSV_ANIMALS)

# Attempt to run the DDLs
run_sql(DB_PARAMS, DDL_SQL_SCRIPT)

# Attempt to insert data
csv_to_table(DB_PARAMS, DATA_CSV_SPONSORED_ANIMALS, 'sponsored_animals')
csv_to_table(DB_PARAMS, DATA_CSV_AGE_COSTS, 'age_costs')
csv_to_table(DB_PARAMS, DATA_CSV_LOCATION_COSTS, 'location_costs')
csv_to_table(DB_PARAMS, DATA_CSV_SIZE_COSTS, 'size_costs')
csv_to_table(DB_PARAMS, DATA_CSV_ANIMALS, 'animals')
