'''Scatter plot -> Scatter plot is a type of plot that uses Cartesian coordinates to display values for two variables for a set of data. The data is displayed as a collection of points, where each point represents the values of the two variables. Scatter plots are useful for visualizing the relationship between two variables and identifying patterns or trends in the data.
plt.scatter(x, y, color='color', marker='marker_type', label='label name')'''

import matplotlib.pyplot as plt

#hours_studies = [1, 2, 3, 4, 5, 6, 7, 8]
#exam_scores = [50, 55, 60, 65, 70, 75, 80, 85]

# Create a scatter plot
plt.scatter([1, 2, 3, 4, 5, 6, 7, 8], [50, 55, 60, 65, 70, 75, 80, 85], color='blue', marker='^', label='student Data') #p1
plt.scatter([1, 2, 3, 4, 5, 6, 7, 8], [52, 57, 63, 68, 72, 78, 82, 88], color='red', marker='o', label='student Data 2') #p2
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('comparison of two classes')
plt.legend()
plt.grid(True)
plt.show()