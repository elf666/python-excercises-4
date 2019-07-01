# przy uzyciu matplotlib narysuj wykres prezentujacy cztery serie danych:
#
# 1. liczby od 1 - 100                    data1 = list(range(1,101))
# 2. logarytmy tych liczb (math.log(x))   [math.log(x) for x in data1]
# 3. liczby pomnożone przez swoj logarytm [math.log(x) * x for x in data1]
# 4. liczby podniesione do kwadratu       [x*x for x in data]

import matplotlib.pyplot as plt
import math

seria1 = list(range(1,11))
seria2 = [math.log(x) for x in seria1]
seria3 = [math.log(x) * x for x in seria1]
seria4 = [x**2 for x in seria1]
seria5 = [2**x for x in seria1]

plt.plot(seria1, label="O(n)")
plt.plot(seria2, label="O(log(n))")
plt.plot(seria3, label="O(n * log(n))")
plt.plot(seria4, label="O(n**2)")
plt.plot(seria5, label="O(2**n)")

plt.legend()
plt.show()
