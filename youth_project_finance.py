import pandas as pd
import psycopg2
from sqlalchemy import create_engine
print('test')

excel_file = '/Users/katherinecunniffe/Desktop/pandas_project/youth_centre_project/youth_centre/income.xlsx'
df1 = pd.read_excel(excel_file)
print(df1.head())

try:
    pgconn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='postgres',
        database='postgres')
    print("connected!")
except: 
    print("error")

conn_string = f'postgresql+psycopg2://postgres:postgres@localhost/postgres'
engine = create_engine(conn_string)

df1.to_sql('income', engine, if_exists='replace', index=False)

column_names = list(df1.columns)
print(column_names)


