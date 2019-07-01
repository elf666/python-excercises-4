import pandas as pd

lab1 = 'abcdefg' # list(lab1)
lab2 = 'bcgkydq'
dat1 = [10, 20, 30, 40, 50, 60, 70]
dat2 = [1,2,3,4,5,6,7]

# stworz dwie Series:
# - pierwsza z dat1 i poszczegolnych liter stringa lab1
# - druga z dat2 i poszczegolnych liter stringa lab2
# - dodaj obie serie do siebie i wyswietl

s1 = pd.Series(dat1, list(lab1))
s2 = pd.Series(dat2, list(lab2))
print(s1 + s2)






# import pandas as pd
#
# ser1 = pd.Series(dat1, list(lab1))
# ser2 = pd.Series(dat2, list(lab2))
# print(ser1)
# print(ser2)
# print(ser1 + ser2)
