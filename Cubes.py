import matplotlib.pyplot as plt

"""Create a graph of cubes"""

x_values = list(range(1,5001))
y_values = [y**3 for y in x_values ]

plt.scatter(x_values, y_values, c=y_values,cmap=plt.cm.Greens, edgecolors='none', s=40)

#Set chart title and label axes.
plt.title("Cubic Numbers", fontsize=24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Cubic of Value", fontsize = 14)

#Set size of tick labels
plt.tick_params(axis='both',which = 'major',labelsize = 14)
plt.show()
#plt.savefig('Cubes_plot.png',bbox_inches='tight') #bbox_inches=tight trims the white space