import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Create figure
fig, ax = plt.subplots()

# Function to update histogram
def update(frame):
    ax.clear()  # clear previous histogram

    # Generate random data
    data = np.random.randn(200)

    # Draw histogram
    ax.hist(data, bins=10, edgecolor='black')

    ax.set_title("Dynamic Histogram")
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")

# Animation (updates every 1 second)
ani = FuncAnimation(fig, update, interval=1000)

plt.show()