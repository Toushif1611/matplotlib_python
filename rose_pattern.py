import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

theta = np.linspace(0, 2*np.pi, 2000)
a = 6

# Initial value of n
n0 = 1.0

# Initial curve
r = a * np.sin(n0 * theta)

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='polar')
plt.subplots_adjust(bottom=0.25)

line, = ax.plot(theta, r, color="red")
ax.set_title("Rose Curve")

# Slider axis
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, 'n', 0.1, 10.0, valinit=n0)

# Update function
def update(val):
    n = slider.val
    r = a * np.cos(n * theta)
    line.set_ydata(r)
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()