import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 25, 15, 30, 20]

plt.bar(categories, values)

plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart")

plt.show()