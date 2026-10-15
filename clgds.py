import pandas as pd
from sqlalchemy import URL,create_engine

excel_file= "clgDS.xlsx"
all_sheets =pd.read_excel(excel_file, sheet_name = None)    


connection_url = URL.create(    
    "mssql+pyodbc",
    host="localhost",   
    database="collage_info",
    query={
        "driver": "ODBC Driver 18 for SQL Server",  
        "TrustServerCertificate": "yes",
    },
)
engine = create_engine(connection_url)

print (all_sheets)
for sheetname, df in all_sheets.items():
            # Use sheet name as table name (replace spaces with underscores)
    #table_name = sheetname.replace(" ", "_")
    df.to_sql(sheetname, con=engine, if_exists="append", index=False)
    print(f"Table '{sheetname}' updated successfully!")

print("✅ Database updated successfully from ALL Excel sheets using SQLAlchemy + SQL Server!")