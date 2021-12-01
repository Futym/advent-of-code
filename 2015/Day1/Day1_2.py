floor = 0
count=0
file = open("Day1/Day1.txt")
while True:
    c=file.read(1)
    count+=1
    if(c==")"):
        floor-=1
    if(c=="("):
        floor+=1
    if(floor<0):
        end=count
        break
    
    if(not c):
        break
print(end)