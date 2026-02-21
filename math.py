import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

xstart = -2
xstop = 2
increment = 0.01

x = np.arange(xstart, xstop, increment)

# Initial value of n
n0 = 1.0

# Initial curve
y = np.abs(x) * np.sin(np.abs(x) + n0)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

line, = ax.plot(x, y, color="red")

ax.set_title("bird")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Slider axis
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, 'n', 0.1, 10.0, valinit=n0)

# Update function
def update(val):
    n = slider.val
    y = np.abs(x) * np.sin(np.abs(x) + n)
    line.set_ydata(y)
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()