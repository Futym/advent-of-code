floor = 0
file = open("Documents/AdventOfCode/2015/Day1/Day1.txt")
while True:
    c=file.read(1)
    if(c==")"):
        floor-=1
    if(c=="("):
        floor+=1
    if(not c):
        break
print(floor)
#with open("Documents/AdventOfCode/2015/Day1/Day1.txt") as file:
    #for line in file:
        #for char in line:
            #if(char==")"):
                #floor-=1
            #if(char=="("):
                #floor+=1
