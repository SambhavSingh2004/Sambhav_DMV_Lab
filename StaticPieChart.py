import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [25, 30, 20, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.title("Static Pie Chart")

plt.show()