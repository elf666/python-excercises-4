import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('cars.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(int(row[1]))

plt.bar(x,y, label='Loaded from file!')
plt.xlabel('samochody')
plt.ylabel('oceny')
plt.title('Oceny samochodow roznych marek')
plt.legend()
plt.show()
