import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Make a random walk and plot the points
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Set the size of the plotting window
    plt.figure(dpi = 128, figsize=(10, 6))

    # Remove the axes.
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    # Making a list of the number of points for the color map (cmap)
    #point_numbers = list(range(rw.num_points))


    plt.plot(rw.x_values, rw.y_values,
                color = 'blue', linewidth=1)

    #Emphasize the first and last points.
    #plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    #plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors = 'none',s=100)



    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
