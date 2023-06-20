import pandas as pd
import psycopg2
from sqlalchemy import create_engine
print('test')

#read in excel file income_alias with six sheets
excel_file = '/Users/katherinecunniffe/Desktop/pandas_project/youth_centre_project/youth_centre/income_alias.xlsx'

excel_data = pd.read_excel(excel_file, sheet_name=None)
df2017_18 = excel_data['2017-18']
df2018_19 = excel_data['2018-19']
df2019_20 = excel_data['2019-20']
df2020_21 = excel_data['2020-21']
df2021_22 = excel_data['2021-22']


#test
print(df2017_18.head())

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

df2017_18.to_sql('2017-18', engine, if_exists='replace', index=False)

column_names = list(df2017_18.columns)
print(column_names)

#how much in total is raised each year via Fundraiser
#how much in total is raised each year Direct
#how much in total is raised each year
#which source IDs donate every year, then via Fundraiser or Direct
#list top largest donator source ID in descending order for each year, what proportion of these are via Fundraiser, are any of these in multible years


