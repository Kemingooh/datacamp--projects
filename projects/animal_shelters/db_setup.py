import os
import sys
import psycopg2

db_params = {
    "host": "localhost",
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres"
}

# External fieles, relative paths to the script location!
DDL_SQL_SCRIPT = 'assets/ddl/createdb.sql'
DATA_CSV_SPONSORED_ANIMALS = 'assets/data/sponsored_pets.csv'
DATA_CSV_AGE_COSTS = 'assets/data/age_costs.csv'
DATA_CSV_LOCATION_COSTS = 'assets/data/location_costs.csv'
DATA_CSV_SIZE_COSTS = 'assets/data/size_costs.csv'
DATA_CSV_ANIMALS = 'assets/data/animal_data.csv'


def csv_to_table(file, conn, cursor, table_name):
    print(f"Loading data from '{file}' into '{table_name}'")
    try:
        with open(file) as csv_file:
            next(csv_file)
            cursor.copy_from(csv_file, table_name, sep=',')
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        conn.close()
        print(error)
        exit(1)
    print("Done")

# Attempt to establish connection with db
print("Establishing connection with DB")
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
except (Exception, psycopg2.DatabaseError) as error:
    print("Failed to connect to the db cluster..")
    print(error)
    exit(1)
print("Done")

# Recreate the tables
print("Recreating tables..")
ddl_script = os.path.join(os.path.dirname(__file__), DDL_SQL_SCRIPT)
with open(ddl_script, 'r') as create_db_sql:
    try:
        cursor.execute(create_db_sql.read())
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        conn.close()
        print(f"Failed to run ddl script '{ddl_script}'..")
        print(error)
        exit(1)
print("Done")

# Absolute file paths
DATA_CSV_SPONSORED_ANIMALS = os.path.join(os.path.dirname(__file__), DATA_CSV_SPONSORED_ANIMALS)
DATA_CSV_AGE_COSTS = os.path.join(os.path.dirname(__file__), DATA_CSV_AGE_COSTS)
DATA_CSV_LOCATION_COSTS = os.path.join(os.path.dirname(__file__), DATA_CSV_LOCATION_COSTS)
DATA_CSV_SIZE_COSTS = os.path.join(os.path.dirname(__file__), DATA_CSV_SIZE_COSTS)
DATA_CSV_ANIMALS = os.path.join(os.path.dirname(__file__), DATA_CSV_ANIMALS)

# Attempt to insert data
csv_to_table(DATA_CSV_SPONSORED_ANIMALS, conn, cursor, 'sponsored_animals')
csv_to_table(DATA_CSV_AGE_COSTS, conn, cursor, 'age_costs')
csv_to_table(DATA_CSV_LOCATION_COSTS, conn, cursor, 'location_costs')
csv_to_table(DATA_CSV_SIZE_COSTS, conn, cursor, 'size_costs')
csv_to_table(DATA_CSV_ANIMALS, conn, cursor, 'animals')

conn.close()
