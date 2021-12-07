import math
file=open("Day7/Day7.txt")
positions=file.readline().replace(","," ").split()
for item in range(len(positions)):
    positions[item]=int(positions[item])
fuel=0
positions.sort()
print(positions)
mediana=positions[math.floor(len(positions)/2)]
for item in positions:
    fuel+=abs(item-mediana)
print(fuel)