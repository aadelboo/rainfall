#import matplotlib.pyplot module
import matplotlib.pyplot as plt

#create a list of rainfall for Brussels and London
rainfall_brussels = [150, 164, 137, 149, 139, 205, 144, 170, 140, 170, 169, 180]
rainfall_london = [188, 153, 229, 173, 192, 273, 261, 134, 157, 169, 192, 157]

#assign the length of the list brussels to the variable x
#move each bar of london to the right by 1
x_brussels = [position * 2 for position in range(len(rainfall_brussels))]
x_london = [position + 1 for position in x_brussels]

#define the height of each bar and subtract 100, assuming there is no rainfall below 100
y_brussels = [length - 100 for length in rainfall_brussels]
y_london = [length - 100 for length in rainfall_london]

#plot the bar chart with value x, y, width, and bottom for each bar
brussels = plt.bar(x_brussels, y_brussels, 0.8, 100)
london = plt.bar(x_london, y_london, 0.8, 100)

#display the bar chart
plt.show()
