import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Line Chart")

plt.subplot(1, 2, 2)
plt.bar(x, y2)
plt.title("Bar Chart")

plt.tight_layout()

plt.show()