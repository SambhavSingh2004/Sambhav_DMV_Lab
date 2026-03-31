import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x), color='blue', lw=2)

ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.1, 1.1)
ax.set_title("Animated Sine Wave")

def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))
    return line,

ani = FuncAnimation(fig, update, frames=100, interval=20, blit=True)

plt.show()