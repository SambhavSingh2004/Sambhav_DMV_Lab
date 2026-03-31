import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

labels = ['A', 'B', 'C', 'D']

fig, ax = plt.subplots()

def update(frame):
    ax.clear()

    sizes = [random.randint(10, 40) for _ in labels]

    ax.pie(sizes, labels=labels, autopct='%1.1f%%')

    ax.set_title("Animated Pie Chart")

ani = FuncAnimation(fig, update, interval=1000)

plt.show()