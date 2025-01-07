#import needed libraries
from sqlalchemy import create_engine
import pandas as pd

pwd = 'seif'  
uid = 'root'    
host = "localhost"
port = 3306 
database = "iti"

# pwd = '123'  
# uid = 'root'    
# host = "localhost"
# port = 3306 
# database = "mart"

def load(df, tbl):
    try:
        # rows_imported = 0
        connection_url = f'postgresql://{uid2}:{pwd2}@{host2}:{port2}/{database2}'
        engine = create_engine(connection_url)
        try:
            src_connpos = engine.connect()
            print("na henaaaa felll dest")
            print(f"Data from {df}:\n")
            
            df.to_sql(name=tbl, con=src_connpos, if_exists="append", index=False)
            print('done')
            df_r = pd.read_sql_query(f"SELECT * FROM {tbl}", src_connpos)
            print(f"Data from {tbl}:\n", df_r)

        except Exception as e:
            raise Exception(f"Connection failed: {str(e)}")

        
    except Exception as e:
        print("Data load error: " + str(e))


def transform(df, table_name):
    
    if table_name == "salesFact":
        df['salesdate'] = pd.Timestamp.today().strftime('%Y-%m-%d')
    return df
def extract():
    try:
        connection_url = f"mysql+pymysql://{uid}:{pwd}@{host}:{port}/{database}"
        src_engine = create_engine(connection_url)

        try:
            src_conn = src_engine.connect()
            print("Connection successful")
        except Exception as e:
            raise Exception(f"Connection failed: {str(e)}")
        
        customerdf= pd.read_sql_query("select customerID , customerName from customer ",src_conn)

        storesdf = pd.read_sql_query("select storeID , storeName from stores ",src_conn)
        
        salesdf = pd.read_sql_query("select customerID , storeID , qty from sales", src_conn)
        
        # print(f"Data from {customerdf}:\n")
        # print(f"Data from {storesdf}:\n")
        # print(f"Data from {salesdf}:\n")



        transform(salesdf,"salesFact")
        load(customerdf,"custDim")
        load(storesdf,"storesDim")
        load(salesdf,"salesFact")
    

    except Exception as e:
        print(f"Data extract error: {str(e)}")
    finally:
        if 'src_conn' in locals() and src_conn:
            src_conn.close()
            print("Connection closed")

# uid2="otifi"
# pwd2="123"
# host2 = "localhost"
# port2 = 5432  
# database2 = "porj"

uid2="etl"
pwd2="admin"
host2 = "localhost"
port2 = 5432  
database2 = "iti"


try:
    extract()
except Exception as e:
    print("Error while extracting data: " + str(e))
