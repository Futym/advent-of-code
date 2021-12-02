file=open("Day2/Day2.txt")
depth=0
forward=0
aim=0
while True:
    inst=file.readline()
    if(inst):
        inst=inst.split()
        if(inst[0]=="up"):
            aim-=int(inst[1])
        if(inst[0]=="down"):
            aim+=int(inst[1])
        if(inst[0]=="forward"):
            forward+=int(inst[1])
            depth+=aim*int(inst[1])
    else:
        break
print(depth*forward)