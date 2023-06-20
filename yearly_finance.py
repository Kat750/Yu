import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


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

dataframes = [df2017_18, df2018_19, df2019_20, df2020_21, df2021_22]
years = ['2017-18', '2018-19', '2019-20', '2020-21', '2021-22']
totals = []

for year, df in zip(years,dataframes):
    total_fundraiser = df.iloc[:, 2].sum()  # Assuming 'Donation via Fundraiser' is the third column (index 2)
    totals.append(total_fundraiser)
    print(f'Total Fundraiser for {year}: {total_fundraiser}')

# Use the total fundraiser values stored in the list called 'totals'
years = ['2017-18', '2018-19', '2019-20', '2020-21', '2021-22']

# Create a pandas DataFrame from the years and totals
df_years_totals = pd.DataFrame({'Year': years, 'Total Fundraiser': totals})

# Plotting the data
df_years_totals.plot(x='Year', y='Total Fundraiser', kind='bar', rot=0)

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Total Fundraiser')
plt.title('Total Fundraiser by Year')

# Display the plot
plt.show()
#how much in total is raised each year Direct
#how much in total is raised each year
#which source IDs donate every year, then via Fundraiser or Direct
#list top largest donator source ID in descending order for each year, what proportion of these are via Fundraiser, are any of these in multible years
#visualise data


