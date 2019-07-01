# skopiuj DataFrame z poprzedniego zadania (ex6) (wlacznie z kolumna V)
# (nie usuwaj rzedow i kolumn)
#
# wypisz DataFrame w ktorym wartosci w kolumnie V sa podzielne przez 3
#
# wypisz tylko rzedy, ktorym wartosci w kolumnie V sa podzielne przez 3 ORAZ
# wartosci w kolumnie III sa podzielne przez 5

import numpy as np
import pandas as pd

my_list = list(range(1,21))
my_array = np.array(my_list)
my_matrix = my_array.reshape(5,4)
x_labels = ['first', 'second', 'third', 'fourth', 'fifth']
y_labels = ["I", "II", "III", "IV"]
my_df = pd.DataFrame(my_matrix, x_labels, y_labels)
my_df['V'] = my_df['I'] + my_df['II']
print(my_df)
print('***')
print(my_df[my_df['V'] % 3 == 0])
print('***')
print(my_df[(my_df['V'] % 3 == 0) & (my_df['III'] % 5 == 0)])






# import numpy as np
# import pandas as pd
#
# x_labels = ['first', 'second', 'third', 'fourth', 'fifth']
# y_labels = ["I", "II", "III", "IV"]
# my_list = list(range(1,21))
# my_array = np.array(my_list)
# my_matrix = my_array.reshape(5,4)
#
# my_df = pd.DataFrame(my_matrix, x_labels, y_labels)
# my_df['V'] = my_df['I'] + my_df['II']
# print(my_df)
#
# print(my_df)
# print(my_df[my_df['V'] % 3 == 0])
# print(my_df[(my_df['V'] % 3 == 0) & (my_df['III'] % 5 == 0)])
