import matplotlib.pyplot as plt
import numpy as np

#fig, ax = plt.subplots()  # Create a figure containing a single axes.
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

# OR

#plt.plot([1, 2, 3,], [2, 4, 1])
#plt.show()

#fig = plt.figure() #blank (fig 1)
#fig, ax = plt.subplots() #plot from line 16 shows (fig 2)
# you don't need plt.show() right after this, no idea why 
#fig, axs = plt.subplots(2,2) #four blank plots with axes show (fig 3)
#ax.plot([1, 2, 3], [2, 1, 2])
#plt.show()

#changing styles
#print(plt.style.available) #prints ones available 
#plt.style.use('tableau-colorblind10')

plt.xkcd()

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x, dev_y, label = "all devs") #color='#444444', linestyle='--', marker='o', hex: red, red, green, green, blue, blue
plt.plot(ages_x, py_dev_y, label='python') #'-.*', color='#5a7d9a', 
plt.plot(ages_x, js_dev_y, label='javascript') #color="#adad3b", linewidth=3,

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary by Age')

plt.legend() #you need this if you want the labels to show

#plt.grid(True)

plt.tight_layout() #margins?/make it look nice if it looked squished

#plt.savefig('plot.png') #saves in current directory, can use any path in ''

plt.show()
