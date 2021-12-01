import matplotlib.pyplot as plt

x_values = list(range(1,1000))
y_values = [x**2 for x in x_values]    #cmap makes a color map gradient
plt.scatter(x_values, y_values, c=y_values,cmap=plt.cm.Greens, edgecolors='none', s=10)

#Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

#Set size of tick labels
plt.tick_params(axis='both',which = 'major',labelsize = 14)
plt.axis([0,1100,0,1100000])
plt.savefig('squares_plot.png',bbox_inches='tight') #bbox_inches=tight trims the white space