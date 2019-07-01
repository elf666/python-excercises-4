import matplotlib.pyplot as plt

# Wyswietlanie jednej serii danych
# dane1 = list(range(1,11))
# dane2 = [x**3 for x in dane1]
# dane3 = list(range(1,50,3))
# plt.plot(dane1)                     # wyswietl dane
# plt.plot(dane1, color='red', label="Dane testowe") # wyswietl dane, nadaj im nazwe
# plt.grid(color='lightblue', linestyle='-.', linewidth=0.5) # float in points
# plt.legend()                         # wyswietl legende
# plt.savefig('output.png', dpi=300)   # zapisz wykres z podana rozdzielczoscia
# plt.show()                           # wyswietl na ekran

## Wyswietlanie > 1 serii danych
dane1 = list(range(1,11))
dane2 = [x**3 for x in dane1]

plt.plot(dane1,dane2) # dane2 = f(dane1)
# plt.plot(dane1, label="Kolejne liczby naturalne")
# plt.plot(dane2, label="Liczy podniesione do szescianu")
# plt.legend()
plt.show()

# I jeszcze cos bardzo uzytecznego..
# with plt.xkcd():
#     plt.plot(dane1)
#     plt.plot(dane2)
#     plt.show()

# ex1_matplotlib_plot.py
