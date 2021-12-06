file=open("Day5/Day5.txt")
floor=[0]*1000
for i in range(1000):
    floor[i]=[0]*1000
count=0
while(True):
    line=file.readline()
    if line:
        line=line.replace(","," ").replace(" -> "," ").split()
        print(str(count)+ " "+ line[0])
        count+=1
        if(line[0]==line[2]):
            if(int(line[1])>=int(line[3])):
                for item in range(int(line[3]),int(line[1])+1):
                    floor[int(line[0])][item]+=1
            else:
                for item in range(int(line[1]),int(line[3])+1):
                    floor[int(line[0])][item]+=1
        elif(line[1]==line[3]):
            if(int(line[0])>=int(line[2])):
                for item in range(int(line[2]),int(line[0])+1):
                    floor[item][int(line[1])]+=1
                    
            else:
                for item in range(int(line[0]),int(line[2])+1):
                    floor[item][int(line[1])]+=1
        else:
            if(int(line[0])>=int(line[2]) and int(line[1])>=int(line[3]) ):   #right-left bottom-top
                counter=0
                for item in range(int(line[2]),int(line[0])+1):
                    floor[int(line[2])+counter][int(line[3])+counter]+=1
                    counter+=1
                    
            if(int(line[2])>=int(line[0]) and int(line[1])>=int(line[3]) ):   #left-right bottom-top
                counter=0
                for item in range(int(line[0]),int(line[2])+1):
                    floor[int(line[0])+counter][int(line[1])-counter]+=1
                    counter+=1
                    
            if(int(line[0])>=int(line[2]) and int(line[3])>=int(line[1]) ):   #right-left top-bottom
                counter=0
                for item in range(int(line[2]),int(line[0])+1):
                    floor[int(line[0])-counter][int(line[1])+counter]+=1
                    counter+=1
                    
            if(int(line[2])>=int(line[0]) and int(line[3])>=int(line[1]) ):   #left-right top-bottom
                counter=0
                for item in range(int(line[0]),int(line[2])+1):
                    floor[int(line[0])+counter][int(line[1])+counter]+=1
                    counter+=1
                    

    else:
        break
count=0
for row in floor:
    for item in row:
        if item>=2:
            count+=1
print(count)