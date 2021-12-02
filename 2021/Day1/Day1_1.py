count = 0
file = open("Day1/Day1.txt")
previous=int(file.readline())
while True:
    now = file.readline()
    if(not now):
        break
    now = int(now)
    if(now>previous):
        count+=1
    previous=now
print(count)