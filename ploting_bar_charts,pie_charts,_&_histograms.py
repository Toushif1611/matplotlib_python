'''DATA VISUALIZATION TOOLS AND THEIR PURPOSES

Bar Charts -> Used to compare different categories or groups by representing data with rectangular bars. Each bar's length is proportional to the value it represents, making it easy to see differences between categories.
plt.bar(x, value, color='color', width=bar_width, label='label name')
Pie Charts -> Used to show the proportions of a whole by dividing a circle into slices. Each slice represents a category's contribution to the total, making it easy to visualize relative sizes of parts to the whole.
plt.pie(values, labels=category_labels, colors=color_list, autopct='%1.1f%%', startangle=angle)
Histograms -> Used to represent the distribution of numerical data by dividing the data into bins or intervals. Each bar represents the frequency of data points within each bin, helping to visualize the shape and spread of the data distribution.
plt.hist(data , bins=number_of_bins, color='color', edgecolor='edge_color', label='label name')
'''

import matplotlib.pyplot as plt

#product = ['A', 'B', 'C', 'D']
#sales = [1000, 1500, 800, 1200]

scores =[45,67,89,56,78,90,34,23,45,67,89,90,77,67,73,89,66,74,85,59]

#plt.barh(product, sales, color='skyblue', label='Sale 2026')
#plt.pie(sales, labels=product, colors=['red', 'blue', 'green', 'orange'], autopct='%1.1f%%', startangle=140)
plt.hist(scores, bins=5, color='lightgreen', edgecolor='black', label='Scores Distribution')
plt.ylabel('Score Ranges')
plt.xlabel('Number of Students')
plt.title('Scores Distribution of Students')
plt.legend()
plt.show()