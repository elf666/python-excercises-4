# wiecej typow wykresow: https://matplotlib.org/gallery/index.html

import matplotlib.pyplot as plt

percents = [35, 35, 30]
# percents = [35, 35, 50]
colors = ['green', 'blue', 'orange']
labels = ['polska', 'zagranica', 'remont']
explode = [0, 0, 0.1]

fig1, ax1 = plt.subplots()
ax1.pie(percents, labels=labels, colors=colors, autopct='%1.1f%%', explode=explode, startangle=90)

plt.title("Gdzie spędzamy wakacje?")
plt.show()

# ex3_matplotlib_pie.py
