file = open("Day3/Day3.txt")
x1=0
y1=0
x2=0
y2=0
listOfHomes=set()
while True:
    direction=file.read(1)
    if direction:
        if(direction=="<"):
            x1-=1
        if(direction==">"):
            x1+=1
        if(direction=="^"):
            y1+=1
        if(direction=="v"):
            y1-=1
    else:
        break
    listOfHomes.add((x1,y1))
    direction=file.read(1)
    if direction:
        if(direction=="<"):
            x2-=1
        if(direction==">"):
            x2+=1
        if(direction=="^"):
            y2+=1
        if(direction=="v"):
            y2-=1
    else:
        break
    listOfHomes.add((x2,y2))
print(len(listOfHomes))
