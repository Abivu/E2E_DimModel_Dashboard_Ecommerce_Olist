import mysql.connector
from Scripts.transform_load_scripts import *

# database credentials
host = "localhost"
user = "root"
password = "1234"

# Lists of the tables
dict_dim_tables = {
    DimCustomer_script: DimCustomer,
    DimSeller_script: DimSeller,
    DimProduct_script: DimProduct,
    DimOrderStatus_script: DimOrderStatus,
    DimPayMethod_script: DimPayMethod,
    DimDate_script: DimDate,
    DimGeolocation_script: DimGeolocation
}

dict_fact_tables = {
    FactOrderItem_script: FactOrderItem,
    FactOrderReview_script: FactOrderReview
}

def populate_olap_tables(dic, cursor, batch_size, offset):
    """
    Function to populate the OLAP tables
    """
    for key in dic:
        cursor.execute(key)
        count = cursor.fetchone()[0]
        print(count, "records found")

    # Loop through the entire table with batch size predefined
    # and offset updated
        while count > 0:
            if count < batch_size:
                batch_size = count
            try:
                cursor.execute(dic[key], (batch_size, offset))
                offset += batch_size
                count -= batch_size
                print(count, "records remaining")
                connection.commit()
            except Exception as error:
                print(f"The connection error details are: {error}")      

    print("The tables have been successfully populated.")



# Establish a connection
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    if connection.is_connected():
        print("Connected to the database")
    # Load the script
        batch_size = 10000
        offset = 0
        cursor = connection.cursor()
        # Count the number of records required to load in OLTP

        populate_olap_tables(dict_dim_tables, cursor, batch_size, offset)
        populate_olap_tables(dict_fact_tables, cursor, batch_size, offset)

finally:
    if connection.is_connected():
        connection.close()
        print("The connection is closed")
