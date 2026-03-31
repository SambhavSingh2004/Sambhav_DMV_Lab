import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

categories = ['A', 'B', 'C', 'D', 'E']

fig, ax = plt.subplots()

values = [random.randint(5, 20) for _ in categories]

bars = ax.bar(categories, values)

ax.set_ylim(0, 30)
ax.set_title("Dynamic Bar Chart")

def update(frame):
    new_values = [random.randint(5, 25) for _ in categories]

    for bar, val in zip(bars, new_values):
        bar.set_height(val)

ani = FuncAnimation(fig, update, interval=1000)

plt.show()