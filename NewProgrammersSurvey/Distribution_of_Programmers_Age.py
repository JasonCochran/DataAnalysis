%matplotlib inline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

programmers_data = pd.read_csv('2016-FCC-New-Coders-Survey-Data.csv')

#Setting up bins for histograms
bins = [10,12.5,15,17.5,20,22.5,25,27.5,30,32.5,35,37.5,40,42.5,45,47.5,50,52.5,55,57.560,62.5,65,67.5,70,72.5,75,77.5,80]

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
plt.yticks(range(0, 2501, 500), [str(x) for x in range(0, 2501, 500)], fontsize=12)    
plt.xticks(fontsize=12)

#Tick lines across graph every 500
for y in range(0, 2501, 500):    
    plt.plot(range(10, 80), [y] * len(range(10, 80)), "--", lw=0.5, color="black", alpha=1)
#Minor ticks every 250 
#for y in range(250, 2501, 500):    
#    plt.plot(range(10, 80), [y] * len(range(10, 80)), "--", lw=0.5, color="black", alpha=0.5)

plt.hist(programmers_data["Age"], bins, histtype = 'bar', width=2.2, alpha=.75)
plt.suptitle("Distribution of Programmers Age", size=20)
plt.xlabel("Age", size=14)
plt.ylabel("Count", size=14)
plt.savefig("Distribution of Programmers Age.png")
