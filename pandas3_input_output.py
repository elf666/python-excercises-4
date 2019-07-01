# csv (comma separated values)
# excel - pip install xlrd
# sql - pip install sqlalchemy

import pandas as pd

# csv read
# from_csv = pd.read_csv('example.csv')
# print(from_csv)

# csv write
# my_df = pd.read_csv('example.csv') # tworzymy DataFrame na podstawie csv
# my_df.to_csv('output.csv', index=True) # drukujemy DataFrame do csv
#
#
# # read excel
# print(pd.read_excel('some_data.xlsx', sheet_name='Sheet1')) # podajemy arkusz, domyslny jest pierwszy
# #
# my_df = pd.read_excel('some_data.xlsx', sheet_name='Sheet1')
# my_df.to_excel('new_excel.xlsx', sheet_name='ABC', index=False) # mozna podac sheet_name, nie trzeba


# sql
from sqlalchemy import create_engine

# dla kazdego typu bazy SQL uzywa sie innej bibliteki do pandas
# tworzymy przykladowa baze sqlite
# engine = create_engine('sqlite:///:memory:')
# # #
# # # pisanie do SQL
# my_df = pd.read_csv('example.csv')
# my_df.to_sql('my_table', engine)
# # #
# # # czytanie z SQL
# sql_df = pd.read_sql('my_table',con=engine)
# print(sql_df)

# ex9_pandas_dataframes.py
