# pandas zbudowano w opariu o numpy
# umożliwia: analize danych, czyszczenie danych, wizualizacje danych

# pip install pandas
import numpy as np
import pandas as pd

# SERIES - zbudowane w oparciu o arrays z numpy
labels = ['a', 'b', 'c']
data_list = [5,10,15]
arr = np.array(data_list)
data_dict = {'x':10, 'y':20, 'z':30}

# series1 = pd.Series(data=data_list) # tworzy domysle labelki
# # print(series1)
# series1 = pd.Series(data=data_list, index=labels) # tu uzywamy labels
# series1 = pd.Series(data_list, labels) # tak tez zadziala
# # print(series1)
# series1 = pd.Series(arr,labels) # mozna podac array zamiast data_list
# # print(series1)
# # #
# series1 = pd.Series(data_dict) # mozna podac slownik
# print(series1)
#
# odwolywanie sie do elementu z SERIES
# series2 = pd.Series([1,2,3], ['a', 'b', 'c'])
# print(series2)
# print(series2['a'])
#
# series3 = pd.Series(['ala', 'ma', 'kota']) # indeksy automatyczne
# print(series3)
# print(series3[2])
#
# dodawanie serii
series4 = pd.Series([11,22,33], ['x', 'y', 'z'])
series5 = pd.Series([44,55,66], ['x', 'q', 'z'])
print(series4 + series5)

# # ex5_pandas_series.py
