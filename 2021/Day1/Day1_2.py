count = 0
file = open("Documents/AdventOfCode/2021/Day1/Day1.txt")
previous1=int(file.readline())
previous2=int(file.readline())
previous3=int(file.readline())
previous_sum=previous1+previous2+previous3
while True:

    now = file.readline()
    if(not now):
        break
    now = int(now)
    sum=previous_sum-previous1+now
    if(sum>previous_sum):
        count+=1
    previous1=previous2
    previous2=previous3
    previous3=now
    previous_sum=sum
print(count)