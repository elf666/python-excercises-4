# bibliteka do algebry liniowej
# większość bibliotek z dziedziny data-science w Pythonie korzysta z NumPy

import numpy as np

# arrays - odpowiednik list, występują jako wektory i matryce (1D i 2D)
# tworzenie arrays bezposrednio z list
L = [1,2,3,4,5]       # pythonowa lista
arr = np.array(L)     # tworzenie array z listy
# print(L)              # w przeciwienstwie do listy
# print(arr)            # array drukuje sie bez przecinkow

M = [[1,2,3],[4,5,6],[7,8,9]]
mx = np.array(M)     # tworzac array z zagniezdzonej listy otrzymujemy macierz
# print(M)
# print(mx)            # drukuje sie w formie 2D
#
# # tworzenie arrays bezposrednio przy uzyciu arange
arr = np.arange(10)  # dziala podobnie jak range
# print(arr)
arr = np.arange(2,11,3) # mozna uzywac krokow
# print(arr)
#
# # tworzenie array wypełnionej 0 lub 1
arr1 = np.zeros(13)      # jednowymiarowa, 5 elementow
arr2 = np.ones((3,5))   # dwuwymiarowa, 3x3 (pdajemy tuple)
# print(arr1)
# print(arr2)
# print(np.ones(10) * 5)  # wypełnienie samymi piątkami
#
# tworeznie arrays z losowymi numerami
arr = np.random.rand(10) # losowe 10 elementow (0 <= x < 1)
# print(arr)
#
mx = np.random.rand(5,5) # macierz losowych 5x5
# print(mx)

# losowe integery w zakresie
arr = np.random.randint(1,100,3) # 3 liczby z zakresu: 1 <= x < 100
# print(arr)
# #
# reshape
arr = np.arange(25)
mx = arr.reshape(5,5) # musi byc wykonalne
# mx = arr.reshape(5,8) # niewykonalne
# print(mx)
#
# min, max
randarr = np.random.randint(1,100,10)
# print(randarr)
# print(randarr.max()) # najwieksza wartosc w array
# print(randarr.min())# najmniejsza
# #
# # indeks min, indeks max
# print(randarr.argmax()) # indeks najwiekszej
# print(randarr.argmin()) # indeks najmniejszej
# #
# print(randarr.dtype)    # typ danych w array
#
#
# # WYBOR ELEMENTOW Z ARRAYS
#
# arr = np.arange(1,11)
# print(arr)
# print(arr[8]) # wypisz wartosc z indeksu 8
# print(arr[1:5]) # slicing :)
# print(arr[:6]) # od poczatku do 6
# print(arr[6:]) # od 6 do konca
#
# # a tu cos wiecej niz pythonowe listy
#
# arr[:5] = 10 # wypełnianie 10tkami w podanym zakresie
# print(arr)
#
# # i teraz uwaga
arr = np.arange(1,11)
# print(arr)
# slice = arr[:6]
# print(slice)
# slice[:] = 100
# print(slice)
# print(arr) # :O - zmodyfikowalismy oryginalna array!
#
# jak zrobic kopię?
# arr_copy = arr.copy()
# print(arr)
# print(arr_copy)
# arr_copy[:] = 50
# print(arr_copy)
# print(arr)
#
# jak dzialamy na 2D
# mx = np.array([[0,2,4],[6,8,10],[12,14,16]])
# print(mx)
# print(mx[0][0])
# print(mx[2][2])
# # # # jak wydrukować 8?
# print(mx[1,1]) # druga mozliwosc zapisu
#
# # matryca z matrycy
# print(mx[:2,1:]) # rzedy od zero do 2 bez 2, kolumny od 1 do konca
arr = np.arange(9)
mx = arr.reshape(3,3)
# print(mx)
#
# # jak wypisac 0,1/3,4?
# print(mx[:2,:2])
# # jak wypisac 4,5/7,8?
# print(mx[1:,1:])
#
# conditional selection
arr = np.arange(1,11)
# print(arr)
# print(arr > 5) # array of booleans // for element in arr return (element > 5)
# bool_arr = (arr % 2 == 0) # array podzielnych przez 2
# print(bool_arr)
# print(arr[bool_arr]) # filtrowanie array przez array
# # #
# # # # mozemy to skrocic do:
# print(arr[arr % 3 == 0])
#
# # operacje na arrays
arr = np.arange(10)
print(arr)
# print(arr + arr)
# print(arr * 5)
# print(arr * arr)
# print(arr + 100)
#
# # dzielenie przez 0
# print(arr / 0) # nan - not a number, inf - infinity
#
# # wiecej: https://docs.scipy.org/doc/numpy/reference/ufuncs.html
#
# # ex4_numpy.py
