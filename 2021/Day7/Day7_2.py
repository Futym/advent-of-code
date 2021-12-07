import math
file=open("Day7/Day7.txt")
positions=file.readline().replace(","," ").split()
for item in range(len(positions)):
    positions[item]=int(positions[item])
fuel=0
positions.sort()
print(positions)
mid=round((sum(positions)/len(positions)))-1
print(mid)
for item in positions:
    tempfuel=0
    temp=abs(item-mid)
    for i in range(temp):
        tempfuel+=i+1
    fuel+=tempfuel
    
print(fuel)