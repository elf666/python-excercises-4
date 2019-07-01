# stworz array zawierajaca pięć jedynek
# przy jej uzyciu stworz array zawierającą pięć piątek
# stworz array skladajaca sie z 30 kolejnych liczb zaczynajac od 3
# stworz z niej macierz 5x6
# przy uzyciu slicow wypisz z powyzszej macierzy kwadrat z liczbami: 9,10/15,16
# stworz macierz  4x6 z 24 losowych liczb z przedzialu 1-100
# wypisz z niej macierz 3x3 elementow z prawego gornego rogu


import numpy as np

# stworz array zawierajaca pięć jedynek
# print(np.ones(5))
#
# # stworz array zawierającą pięć piątek
# print(np.ones(5) * 5)
#
# # stworz array skladajaca sie z 30 kolejnych liczb zaczynajac od 3
x = np.arange(3,33)
print(x)
#
# stworz z niej macierz 5x6
m = x.reshape(5,6)
print(m)

# # przy uzyciu slicow wypisz z powyzszej macierzy kwadrat z liczbami: 9,10/15,16
print(m[1:3, :2])
#
# stworz macierz 4x6 24 losowych liczb z przedzialu 1-100
mr = np.random.randint(1,101,24).reshape(4,6)
print(mr)
#
# # # wypisz z niej macierz 3x3 elementow z prawego gornego rogu
print(mr[:3, 3:])
