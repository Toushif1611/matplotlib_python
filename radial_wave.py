import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# Range
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Constant
A = 1.0
K = 1.0
w = 1.0
t = 1.0

X, Y = np.meshgrid(x, y)

# Initail wave
Z = A*np.sin(K*np.sqrt(X**2 + Y**2) + w*t)

# Figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis')

ax.view_init(elev=30, azim=45)

# Slider
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

axA = plt.axes([0.2, 0.20, 0.6, 0.03])
axK = plt.axes([0.2, 0.15, 0.6, 0.03])
axW = plt.axes([0.2, 0.10, 0.6, 0.03])
axT = plt.axes([0.2, 0.05, 0.6, 0.03])

sliderA = Slider(axA, 'Amplitude', -5.0, 5.0, valinit=A)
sliderK = Slider(axK, 'Wavelength', -5.0, 5.0, valinit=K)
sliderW = Slider(axW, 'Frequency', -5.0, 5.0, valinit=w)
sliderT = Slider(axT, 'Time', -5.0, 5.0, valinit=t)

# Update Function
def update(val):
    A = sliderA.val
    K = sliderK.val
    w = sliderW.val
    t = sliderT.val
    
    Z = A*np.sin(K*np.sqrt(X**2 + Y**2) + w*t)
    
    ax.clear()
    ax.plot_surface(X, Y, Z, cmap='viridis')
    fig.canvas.draw_idle()

sliderA.on_changed(update)
sliderK.on_changed(update)
sliderW.on_changed(update)
sliderT.on_changed(update)

plt.show()