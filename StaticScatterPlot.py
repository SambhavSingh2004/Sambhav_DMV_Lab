import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

plt.scatter(x, y)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot with Grid")

plt.grid(True)

plt.show()