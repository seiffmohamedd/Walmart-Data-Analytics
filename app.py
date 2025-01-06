#import needed libraries


from sqlalchemy import create_engine
import pandas as pd

pwd = 'seif'  
uid = 'root'    
host = "localhost"
port = 3306 
database = "seif"

mysql_user = 'root'
mysql_password = '123'
mysql_host = '127.0.0.1'
mysql_database = 'mart'

def extract():
    try:
        # connection_url = f"mysql+pymysql://{uid}:{pwd}@{host}:{port}/{database}"
        # src_engine = create_engine(connection_url)
        src_engine = create_engine(f'mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_database}')  ###otifi

        try:
            src_conn = src_engine.connect()
            print("Connection successful")
        except Exception as e:
            raise Exception(f"Connection failed: {str(e)}")

        query = """
        SELECT TABLE_NAME AS table_name
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = 'mart'
        AND TABLE_NAME IN ('stores')
        """
        src_tables = pd.read_sql_query(query, src_conn).to_dict().get('table_name', {})

        for id, table_name in src_tables.items():
            df = pd.read_sql_query(f"SELECT * FROM {table_name}", src_conn)
            print(f"Data from {table_name}:\n", df)
            # load(df, table_name)

    except Exception as e:
        print(f"Data extract error: {str(e)}")
    finally:
        if 'src_conn' in locals() and src_conn:
            src_conn.close()
            print("Connection closed")

uid2="etl"
pwd2="admin"
host2 = "localhost"
port2 = 5432  
database2 = "iti"

def load(df, tbl):
    try:
        # rows_imported = 0
        connection_url = f'postgresql://{uid2}:{pwd2}@{host2}:{port2}/{database2}'
        engine = create_engine(connection_url)
        try:
            src_conn = engine.connect()
            print("Connection postgres successful")
            table_name = 'student'
            df.to_sql(name=table_name, con=src_conn, if_exists="append", index=False)
            print('done')
            df_r = pd.read_sql_query(f"SELECT * FROM {table_name}", src_conn)
            print(f"Data from {table_name}:\n", df_r)

        except Exception as e:
            raise Exception(f"Connection failed: {str(e)}")

        # print(f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}')
        # df.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False, chunksize=100000)
        # rows_imported += len(df)my
        # print("Data imported successful")
        # print('done')
    except Exception as e:
        print("Data load error: " + str(e))

try:
    extract()
except Exception as e:
    print("Error while extracting data: " + str(e))
