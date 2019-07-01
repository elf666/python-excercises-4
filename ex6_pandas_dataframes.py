# utworz liste kolejnych liczb od 1 - 20 (range)
# utworz z niej array (np.array(jakas lista))  # import numpy as np
#
# przy uzyciu numpy utworz z array macierz 5x4 #(jakas_array.reshape(X x Y))
#
# uzywajac tej macierzy stworz DataFrame:      # import pandas as pd
# ktora w rzedach ma indeksy  ['first', 'second', 'third', 'fourth', 'fifth']
# a w kolumnach indeksy ["I", "II", "III", "IV"]
#
# dodaj kolumnę 'V' ktora sumuje zawartosc kolumn 'I' i 'II'
# usun permanentnie kolumne 'III' #(inplace=True, axis=1)
# usun permanentnie rzad 'third'


import numpy as np
import pandas as pd

my_list = list(range(1,21))
my_array = np.array(my_list)
my_matrix = my_array.reshape(5,4)

x_labels = ['first', 'second', 'third', 'fourth', 'fifth']
y_labels = ["I", "II", "III", "IV"]

my_df = pd.DataFrame(my_matrix, x_labels, y_labels)
print(my_df)

my_df['V'] = my_df['I'] + my_df['II']
print(my_df)

my_df.drop('III', axis=1, inplace=True)
my_df.drop('third', inplace=True)
print(my_df)
