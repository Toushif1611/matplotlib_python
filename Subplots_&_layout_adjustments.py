#plt.subplot(rows, columns, index)

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

"""plt.subplot(1, 2, 1) # 1 row, 2 columns, first plot
plt.plot(x, y)
plt.title('line chart')

plt.subplot(1, 2, 2) # 1 row, 2 columns, second plot
plt.bar(x, y)
plt.title('bar chart')

#plt.tight_layout() # Adjusts the spacing between subplots to prevent overlap
plt.show()"""

#Fig, Axes = plt.subplots(nrows=2, ncols=2, figsize=(widht, height)) # Creates a 2x2 grid of subplots

fig, ax = plt.subplots(1, 2, figsize = (10,5))

ax[0].plot(x,y, color="red")
ax[0].set_title('Line plot')
ax[1].bar(x,y, color="green")
ax[1].set_title('Bar chart')

fig.suptitle("comparision of line and bar chart")
plt.tight_layout()
plt.show()
