import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# Range
x = np.arange(-2, 2, 0.05)
y = np.arange(-2, 2, 0.05)
X, Y = np.meshgrid(x, y)

# Constants
A = 1.0
K = 1.0
W = 1.0
T = 1.0

# Initial wave
Z = A * np.sin(K * np.sqrt(X**2 + Y**2) + W*T)

# Figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.3)

surf = ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_title("Radial Wave")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Sliders
axA = plt.axes([0.2, 0.20, 0.6, 0.03])
axK = plt.axes([0.2, 0.15, 0.6, 0.03])
axW = plt.axes([0.2, 0.10, 0.6, 0.03])
axT = plt.axes([0.2, 0.05, 0.6, 0.03])

sliderA = Slider(axA, 'A', 0.1, 5.0, valinit=A)
sliderK = Slider(axK, 'K', 0.1, 5.0, valinit=K)
sliderW = Slider(axW, 'W', 0.1, 5.0, valinit=W)
sliderT = Slider(axT, 'T', 0.1, 5.0, valinit=T)

# Update function
def update(val):
    A = sliderA.val
    K = sliderK.val
    W = sliderW.val
    T = sliderT.val
    
    ax.clear()
    Z = A * np.sin(K * np.sqrt(X**2 + Y**2) + W*T)
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title("Radial Wave")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

sliderA.on_changed(update)
sliderK.on_changed(update)
sliderW.on_changed(update)
sliderT.on_changed(update)

plt.show()