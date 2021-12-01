file = open("Day2/Day2.txt")
sum=0
while True:
    box=file.readline()
    if(box):
        box=box.split("x")
        bow=int(box[0])*int(box[1])*int(box[2])
        maxside=max(int(box[0]),int(box[1]),int(box[2]))
        for x in range(0,3):
            sum+=2*int(box[x])
    else:
        break
    sum+=bow-2*maxside
print(sum)