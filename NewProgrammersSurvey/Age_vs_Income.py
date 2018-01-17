%matplotlib inline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

programmers_data = pd.read_csv('2016-FCC-New-Coders-Survey-Data.csv')

#Picking our data.. makes it more
comSci = programmers_data[programmers_data['SchoolMajor'] == "Computer Science"]
noDegree = programmers_data[programmers_data['SchoolDegree'] == "some college credit, no degree"]

#Removing any data that contains NaN entries
comSci = comSci[np.logical_not(np.isnan(comSci["Age"]))]
comSci = comSci[np.logical_not(np.isnan(comSci["Income"]))]
noDegree = noDegree[np.logical_not(np.isnan(noDegree["Age"]))]
noDegree = noDegree[np.logical_not(np.isnan(noDegree["Income"]))]

#Sets size
plt.figure(figsize=(12, 9))

#Style for graph...
ax = plt.subplot(111)    
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)
ax.patch.set_alpha(0.0)
ax.get_xaxis().tick_bottom()    
ax.get_yaxis().tick_left()

#x and y ticks, labels for scale
plt.yticks(range(0, 200001, 50000), [ "$" + str(x) + "k" for x in range(0, 201, 50)], fontsize=14)    
plt.xticks(fontsize=14)

#Tick lines across graph
for y in range(50000, 200001, 50000):    
    plt.plot(range(15, 75), [y] * len(range(15, 75)), "--", lw=0.5, color="black", alpha=0.5) 

plt.ylim([0,200000])
plt.xlim([15,75])

#puts on individual labels for each fit line
plt.text(67, 85000, "No Degree", fontsize=14, color="black")
plt.text(60, 145000, "Computer Science Degree", fontsize=14, color="black")

#Main scatter plots
plt.scatter(comSci["Age"], comSci["Income"], alpha=.1, color='b')
plt.scatter(noDegree["Age"], noDegree["Income"], alpha=.1, color='y')

#Linear regression lines
plt.plot(comSci["Age"], np.poly1d(np.polyfit(comSci["Age"], comSci["Income"], 1))(comSci["Age"]) )
plt.plot(noDegree["Age"], np.poly1d(np.polyfit(noDegree["Age"], noDegree["Income"], 1))(noDegree["Age"]), color='y' )

#Titles and saving
plt.suptitle("Age vs Income", size=20)
plt.title("Programmers with a computer science degree compared to those without a degree."
          "\nComparing age against income.", size = 13)
plt.text(25, -25000, "Data source: https://www.kaggle.com/freecodecamp/2016-new-coder-survey-"
                    "\nAll data without age or income was removed from the set before analysis.",size=11)
plt.savefig("Age vs Income.png")
