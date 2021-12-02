from die import Die
import pygal

#Create two six sided die
die1 = Die()
die2 = Die()


#Make some rolls, and store some results in a list
results = []
for roll_num in range(10000):
    result = die1.roll() + die2.roll()
    results.append(result)

#Analyze the results.
frequencies = []
max_result = die1.num_sides + die2.num_sides
min_result = 2
for value in range(min_result, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling " + str(min_result) + " D6 10000 times."
hist.x_labels = [str(x) for x in range(min_result, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')


print(frequencies)

import matplotlib.pyplot as plt

input_values = [str(x) for x in range(min_result, max_result+1)]
plt.bar(input_values, frequencies, linewidth = 5) #controls thickness of graphed line

#Set chart title and label axes.
plt.title("Results of rolling " + str(min_result) + " D6 10000 times.", fontsize = 24) #creating a title
plt.xlabel("Result", fontsize = 14)
plt.ylabel("Frequency", fontsize=14)

#Set size of tick labels.
plt.tick_params(axis='both',labelsize=14)

plt.show()