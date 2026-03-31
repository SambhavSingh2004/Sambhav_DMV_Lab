import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(150)

plt.hist(data, bins=10, color='blue', edgecolor='black')

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Basic Histogram")

plt.show()