'''Matplotlib Pyplot Function

plt.grid(x, y, color='color', linestyle='linestyle', linewidth=width, marker='marker symbol', label='label name')
plt.xlabel('text')
plt.ylabel('text')
plt.plot()
plt.title()
plt.Legend()
plt.xticks()
plt.yticks()
plt.xlim()
plt.ylim()
plt.show()'''

import matplotlib.pyplot as plt

months = [1, 2, 3, 4]
sales = [1000, 1500, 1200, 1700]

plt.plot(months, sales, color='blue', linestyle='--', marker='o', label='Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')
plt.legend(loc = 'upper left', fontsize='small')
plt.grid(color ='gray', linestyle=':', linewidth=0.5)
plt.xlim(1,4)
plt.xticks([1,2,3,4], ['M1', 'M2', 'M3', 'M4'])
plt.ylim(0, 2000)
plt.show()