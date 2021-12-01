file = open("Day3/Day3.txt")
x=0
y=0
listOfHomes=set()
while True:
    direction=file.read(1)
    if direction:
        if(direction=="<"):
            x-=1
        if(direction==">"):
            x+=1
        if(direction=="^"):
            y+=1
        if(direction=="v"):
            y-=1
    else:
        break
    listOfHomes.add((x,y))
print(len(listOfHomes))
