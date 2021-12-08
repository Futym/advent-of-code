file=open("Day8/Day8.txt")
count=0
while True:
    temp=file.readline()
    if temp:
        temp=temp.replace(" | "," ").split()
        print(temp)
        for x in range(10,14):
            if(len(temp[x])==2):
                count+=1
            if(len(temp[x])==3):
                count+=1
            if(len(temp[x])==4):
                count+=1
            if(len(temp[x])==7):
                count+=1
    else:
        break
print (count)