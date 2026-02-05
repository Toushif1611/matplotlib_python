#savefig("filename.extention", dpi = value, bbox_inches = 'tight')

import matplotlib.pyplot as plt

x = [1,2,3,4]
y=[10,20,15,25]

#create plot
plt.plot(x,y, color = 'blue', marker='o')
plt.title("sample line plot")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.savefig("Line_plot.png", dpi=300, bbox_inches='tight')
plt.show()