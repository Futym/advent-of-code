file = open("Day2/Day2.txt")
sum=0
while True:
    box=file.readline()
    if(box):
        box=box.split("x")
        print(box)
        min=int(box[0])*int(box[1])
        for x in range(0,3):
            for y in range(0,3):
                temp=int(box[x])*int(box[y])
                if(x!=y):
                    sum+=temp
                    if(temp<min):
                        min=temp
    else:
        break
    sum+=min
print(sum)