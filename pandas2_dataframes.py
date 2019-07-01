import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101) # seed do generowania randomowych liczb

df = pd.DataFrame(randn(5,4), list('abcde'), list('PQRS'))
                #(dane, labelki rzędow, labelki kolumn)
# print(df)

# kazda kolumna to Series, ktore maja wspolne indeksy
# wypisywanie kolumn
print(df)
# print(df['P'])        # kolumna, ktora jest typu Series
# print(df.P)           # tez zadziala
# print(df[['P', 'S']]) # podwojne nawiasy: [[ ]]
#
# dodawanie kolumny
# df['new'] = df['R'] + df['S']
# print(df)
#
# usuwanie kolumny
# df.drop('new', axis=1, inplace=True) # axis=1 oznacza, ze chodzi mi o kolumne
# print(df)                            # inplace = True -> usun na stałe z df
# new = df.drop('e') # domyslna axis=0 - czyli chodzi o rząd
# print(new)

# jesli chce zmodyfikowac aktualna tabele to dodaje inplace=True
# df.drop('new', axis=1, inplace=True)
# print(df)
# #
# # wypisywanie rzędów
print(df.loc['c']) # loc - location, wypisuje rzad jako Series, czyli jako kolumne!
print(df.iloc[3])  # iloc - index location, numer indeksu (nawete jesli indeks jest stringiem)

# wypisywanie podzbioru rzad/kolumna (jak w numpy)
# print(df)
# # print(df.loc['b', 'Q'])            # pojedyncza komorka
# print(df.loc[['a','c'],['Q','R']])   # mniejszy DataFrame

# # ex_6_pandas_dataframes.py

# print(df)
#
# conditional selection (jak w numpy)
print(df)
# print(df > 0)
#
# bool_df = df > 0
# # print(bool_df)
# print(df[bool_df]) # zastosuj dataframe booli na dataframe liczb
# print(df[df > 0])  # tak szybciej i prosciej
#
#zwracanie rzedow i kolumn, ktore spelniaja konkretne warunki
# print(df['S'] > 0) # info ktore wartosci kolumny S sa > 0
# print(df[df['R'] < 0]) # wypisz tylko te rzedy, w ktorych wartosci w kolumnie S > 0
#
# wypiszmy wszystkie rzedy, dla ktorych wartosci w Q < 0
# print(df[df['Q'] < 0])
# result = df[df['Q'] < 0] # mozemy w ten sposob stworzyc nowy DataFrame
# print(result[['P', 'Q']]) # i dzialac na nim tak samo jak wczesniej
#
# mozemy wpisac kilka warunkow na raz
# print(df)
# print(df[(df['P']>0) & (df['Q']<0)]) # & = and dla DataFrames
# print(df[(df['S']>0.6) & (df['R']>2)])
# print(df[(pierwszy_warunek)&(drugi_warunek)])

# # a wiec zamiast and uzywamy &, a zamiast or uzywamy | (pipe)
# print(df[(df['P']>0) | (df['Q']<0)])
#
# dodawanie nowych indeksow w formie kolejnych intów
# print(df.reset_index()) # dotychczasowe indeksy staja sie nowa kolumna
#
# tworzenie calkiem nowych indeksow
# new_indexes = list('ABCDE')
# df['new'] = new_indexes
# print(df)
# df.set_index('new', inplace=True) # tworzymy indeksy z nowej kolumny
# print(df) # bedzie brzydko pusty rząd :/
#
# # ex7_pandas_selection.py
#
# Dealing with missing data

my_dict = {'A':[1,2,np.nan], 'B':[5,np.nan, np.nan], 'C':[1,2,3]}
df = pd.DataFrame(my_dict)
print(df)
# #
# drop values
# print(df.dropna()) # drop missing values (rzedy)
# print(df.dropna(axis=1)) # drop missng values (kolumny)
#
# theshold - próg
# print(df.dropna(thresh=2)) # usun rzedy ktore maja minimum 2 nany
#
# fill
print(df.fillna(value='FILL')) # fill with provided values
print(df['A'].fillna(value=df['A'].mean()))
print(df.fillna(value=df.mean())) # wypełnij kolumny srednią dla poszczegolnej kolumny

# ex8_pandas_dataframes.py
