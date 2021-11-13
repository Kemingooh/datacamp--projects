import psycopg2


def __db_connect(db_params):
    # Attempt to establish connection with db
    print("Establishing connection with DB")
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
    except psycopg2.DatabaseError as error:
        print("Failed to connect to the db cluster..")
        print(error)
        exit(1)
    print("Done")
    return conn, cursor


def csv_to_table(db_params, file, table_name):
    conn, cursor = __db_connect(db_params)
    print(f"Loading data from '{file}' into '{table_name}'")
    with open(file, 'r', encoding='utf-8') as csv_file:
        try:
            next(csv_file)
            cursor.copy_from(csv_file, table_name, sep=',')
            conn.commit()
        except psycopg2.DatabaseError as error:
            conn.close()
            print(error)
            exit(1)
        finally:
            conn.close()
    print("Done")


def run_sql(db_params, file):
    conn, cursor = __db_connect(db_params)
    # Recreate the tables
    print("Running ")
    with open(file, 'r', encoding='utf-8') as create_db_sql:
        try:
            cursor.execute(create_db_sql.read())
            conn.commit()
        except psycopg2.DatabaseError as error:
            conn.close()
            print(f"Failed to run ddl script '{file}'..")
            print(error)
            exit(1)
        finally:
            conn.close()
    print("Done")
