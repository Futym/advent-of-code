file=open("Day3/Day3.txt")
param=0
gamma=0
count=[0,0,0,0,0,0,0,0,0,0,0]
zeros=0
ones=1
mystr=""
mystr1=""
lines=file.readlines()
print(lines[0],lines[12][12])
halfLength=len(lines)/2

for line in lines:
    for x in range(0,len(lines[0])-1):
        if(line[x]=="1"):
            count[x]+=1
for x in count:
    if(x>halfLength):
        mystr+="1"
        mystr1+="0"
    else:
        mystr+="0"
        mystr1+="1"
c1=int(mystr,2)
c2=int(mystr1,2)
print(c1*c2)