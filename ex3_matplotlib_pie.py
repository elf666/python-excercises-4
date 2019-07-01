# najpopularniejsze jezyki 2019 wg stacoverflow (jaki procent developerów zna)
# https://insights.stackoverflow.com/survey/2019#key-results
# narysuj wykres kolowy przedstawiajacy udzial 5 najbardziej popularnych jezykow
# programowania w rynku programistycznym
# * wybierz ladny styl kolorow z coolors.co

import matplotlib.pyplot as plt

languages = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
percent_of_devs = [68, 63, 55, 42, 41]
colors = ['#05668D', '#028090', '#00A896', '#02C39A', '#F0F3BD']

fig1, ax1 = plt.subplots()
ax1.pie(percent_of_devs, labels=languages, colors=colors, autopct='%1.1f%%')

plt.title("Najpopularniejsze jezyki programowania w 2019.")
plt.show()
