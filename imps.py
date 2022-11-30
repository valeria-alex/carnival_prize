import matplotlib.pyplot as plt
import numpy as np
import random

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
                                while chance in chances & chance != 0:
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
        return chances


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
 
value = input('Let us start')
if value != None:
    plt.cla()
    #explode = (0, 0.1, 0, 0)
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()