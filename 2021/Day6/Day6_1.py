file=open("Day6/Day6.txt")
fishes=[0 for i in range(9)]
while True:
    fisch=file.read(1)
    if fisch:
        if(fisch!=","):
            fishes[int(fisch)]+=1
    else:
        break
print (fishes)
for counter in range(256):
    temp=fishes[0]
    for i in range(8):
        fishes[i]=fishes[i+1]
    fishes[6]+=temp
    fishes[8]=temp
print(sum(fishes))