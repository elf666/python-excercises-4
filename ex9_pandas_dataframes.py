# google example csv file, first record
# https://people.sc.fsu.edu/~jburkardt/data/csv/homes.csv
#
# przeczytaj plik csv, zapisz go do DataFrame
# wypisz na konsolę zawartosc pliku
# wyizoluj i wypisz kolumnę Taxes
# policz i wypisz jej średnią (srednia - mean())
# zapisz DataFrame z danymi do excela
# użyj linka, nie kopiuj danych



import pandas as pd

home_sells_df = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/homes.csv')
taxes = home_sells_df[' "Taxes"']
print(taxes)
print(f"Average tax payd for single home sell was: {taxes.mean()}$.")
# print(list(home_sells_df.columns.values))

home_sells_df.to_excel('Homes.xlsx')
