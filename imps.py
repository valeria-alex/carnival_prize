import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.widgets import Button


def luck(l=None):
        chances = []
        if l == None:
                print ('please provide a list')
        else:
                #each element is assigned a chance, but the sum of chances across element must be 100
                max = 100
                for i in range(len(l)):
                        
                        chance = random.randint(0,max)
                        if chance in chances:
                                while chance in chances and chance != 0:
                                        chance = random.randint(0,max)
                        
                        #ensure all chances add up to 100
                        if i == len(l) - 1:
                                chance = max
                        else: 
                                max -= chance
                                if max < 0:
                                        max = 0
                        chances.append(chance)
                        print (i, l[i], chance)
                #the highest chance wins
        print ("why does it still go in else")
        return chances

        
def more(winner):
        print (thisdict[str(labels[maxchanceindex])])
        sublabels = thisdict[str(labels[maxchanceindex])]
        subsizes = luck(sublabels)
        submaxchanceindex = np.argmax(subsizes)
        subexplode = [0] * len(sublabels)
        #clear previous plot
        ax1.cla()
        #explode = (0, 0.1, 0, 0)
        ax1.pie(subsizes, explode=subexplode, labels=sublabels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        plt.show()
        # if winner == None:
        #         print ("No winner detected")
        # else:
        #         print ("winning cat", winner)

print ("check python")
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
thisdict = {
  "games": ["Elden Ring", "League of Legends", "Minecraft", "Stray"],
  "video": ["Vlog", "Storytelling", "Cooking"],
  "code":  ["Python", "C++", "scss", "Java", "Typescript"],
  "exercise": ["bike", "gym", "dance", "walk", "bouldering"]
  #"relax": ["movie", "hangout"]
}
labels = list(thisdict.keys())
sizes = luck(labels)#[15, 30, 45, 10]

explode = [0, 0, 0, 0]  # only "explode" the 2nd slice (i.e. 'Hogs')
print (max(sizes))
print (np.argmax(sizes))
maxchanceindex = np.argmax(sizes)
explode[maxchanceindex] = 0.3
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#is this for need more help _   
value = input('Press any key to continue')
axbut = fig1.add_axes([0.86, 0.30, 0.1, 0.075])

if value != None:
    plt.cla()
    #explode = (0, 0.1, 0, 0)
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    bnext = Button(axbut, 'More')
    bnext.on_clicked(more)
    #(thisdict[str(labels[maxchanceindex])])
plt.show()