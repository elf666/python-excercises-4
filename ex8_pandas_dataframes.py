# stworz dataframe o wymiarach 6x6 skladajacy sie z losowych liczb z przedzialu 1-100
# przefiltruj dataframe tak aby zostaly w nim tylko liczby wieksze niz 55 !!!!!!!!!!!
# usun rzedy, w ktorych jest wiecej niz 2 nany
# w pozostalych miejscach DataFrame w miejsce NaNów wpisz średnią wartosc dla danej kolumny
# wydrukuj kazdy kolejny etap obróbki dataframe

import numpy as np
import pandas as pd

mx = np.random.randint(1,101,36).reshape(6,6)
df = pd.DataFrame(mx)
filtered = df[df > 55]
print(filtered)
filtered.fillna(filtered.mean(), inplace=True)
print('******')
print(filtered)
