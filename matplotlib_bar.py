import matplotlib.pyplot as plt

labels = ['koty', 'psy', 'papugi', 'rybki']
data = [100, 200, 150, 15]

plt.bar(labels, data)      # najpierw opis, potem dane
# plt.barh(labels, data)      # najpierw opis, potem dane
plt.bar(labels, data, width=[0.1, 0.2, 0.3, 0.4], bottom=50, color=['red', 'yellow', 'green', 'cyan'])
# dwa wykresy na raz
plt.xlabel('zwierzeta')    # opis osi x
plt.ylabel('ceny')         # opis osi y
plt.title('Ceny w zoologicznym') # dodanie tytulu
plt.show()


# ex2_matplotlib_bar.py
