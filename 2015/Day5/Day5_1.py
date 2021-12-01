from os import truncate


file = open("day5/Day5.txt")
count=0
while True:
    word=file.readline()
    if word:
        vovels=0
        double=False
        exception=False
        previous=None
        for x in word:
            if(x=="a" or x=="e" or x=="o" or x=="i" or x=="u"):
                vovels+=1
            if(x==previous):
                double=True
            if(previous!=None and (previous+x=="ab" or previous+x=="cd" or previous+x=="pq" or previous+x=="xy")):
                exception=True
            previous=x
        if(vovels>=3 and double and not exception):
            count+=1
    else:
        break
print(count)
