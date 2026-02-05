'''KEY TERM YOU SHOULD KNOW

Data Point -> x-axis, y-axis
X-axis / Y-axis -> Horizontal / Vertical axis
Figure -> The entire window or page that holds the plot(s)
Axes -> The area on which data is plotted
Plot -> The visual representation of data (lines, bars, etc.)
Marker -> Symbols used to represent data points(e.g., circles(O), squares(S), diamonds(D), cross(X), pluses(+))
line style -> The appearance of lines in a plot (solid(_), dashed(_ _), dotted(:), dash-dot(_.))
Color -> The color of plot elements (e.g., 'b' for blue, 'g' for green, 'r' for red)
Legend -> A key that explains the symbols, colors, or line styles used in the plot
Labels -> Text that describes the axes or data series in the plot
Title -> The heading of the plot that provides context about the data being visualized
Grid -> A network of lines on the plot that helps in reading values accurately
Function -> A mathematical relationship between two variables, often represented as y = f(x)
Method -> A function that is associated with an object and is called on that object
Parameters -> Values that are passed to functions or methods to customize their behavior
Keyword Arguments -> Named parameters that allow you to specify values for specific parameters in a function or method call
Object-Oriented API -> A programming approach that uses objects and methods to create and manipulate plots, providing more control and flexibility compared to the state-based interface
DPI (Dots Per Inch) -> A measure of the resolution of a plot or image, indicating how many dots fit into one inch
Backend -> The underlying software that handles the rendering of plots, which can vary depending on the environment (e.g., interactive window, file output)
Matplotlib OOA -> Matplotlib's Object-Oriented API, which allows for more advanced and customizable plotting by directly manipulating figure and axes objects
'''

import matplotlib.pyplot as plt
x = ['Mon','Tue','Wed','Thu','Fri'] #x-axis
y= [10, 15, 7, 20, 12] #y-axis

plt.plot(x,y) #plotting the x and y axis

plt.title('Bakery Sales This Week:')

plt.xlabel('Days of the week') #label for x-axis
plt.ylabel('Sales Per Day')

plt.show() #display the plot
