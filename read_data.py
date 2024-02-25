# Import useful libraries & modules
import os
import sys
import pandas as pd 
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


#MySQL database connection parameters
db_user="root"
db_password="1234"
db_host="localhost"
db_name="olist_oltp"
db_port="3306"

# Create a MySQL connection
engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}", echo=True)
session = Session(engine)

# directory contain csv files
csv_dir = "./Olist"

# Get a list of csv files in directory
csv_files = [file for file in os.listdir(csv_dir) if file.endswith(".csv")]

# Loop through each CSV file and load it into the MySQL database
for file in csv_files:
    csv_path = os.path.join(csv_dir, file)

    df = pd.read_csv(csv_path)

    df.columns = df.columns.str.replace(" ","_")

    with engine.connect() as conn:
        df.to_sql(file.replace(".csv",""),
                con=conn,
                if_exists="replace",
                index=False)
# Close MySQL Connection
engine.dispose()


