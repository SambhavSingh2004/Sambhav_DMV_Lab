import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o', linestyle='-', label='y=2x')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Chart with Markers")

plt.legend()
plt.grid(True)

plt.show()