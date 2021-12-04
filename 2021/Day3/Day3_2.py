file=open("Day3/Day3.txt")

zeros=0
ones=1
lines=file.readlines()
lines2=lines

for i in range(0,len(lines[0])):
    
    length=len(lines)/2
    temp=[]
    count=0
    for line in lines:
        if(int(line[i])==1):
            count+=1
    if count>=length:
        temp1=1
    else:
        temp1=0
    for line in lines:
        if(int(line[i])==temp1):
            temp.append(line)
    lines=temp
    if(len(lines)==1):
        break

c1=int(lines[0],2)

lines=lines2
for i in range(0,len(lines[0])):
    
    length=len(lines)/2

    temp=[]
    count=0
    for line in lines:
        if(line[i]=="1"):
            count+=1
    if count>=length:
        temp1=0
    else:
        temp1=1
    for line in lines:
        if(int(line[i])==temp1):
            temp.append(line)
    lines=temp
    if(len(lines)==1):
        break

c2=int(lines[0],2)
print(c1*c2)