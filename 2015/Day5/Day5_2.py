from os import truncate


file = open("day5/Day5.txt")
count=0
while True:
    word=file.readline()
    if word:
        previouspair=None
        secondPreviousPair=None
        doubleDouble=False
        repeatAfterOne=False
        previous=None
        secondPrevious=None
        listOfDoubles = []
        for x in word:
             
            if(previous!=None):
                if not previous+x in listOfDoubles:
                    listOfDoubles.append(previouspair)
                    previouspair=previous+x
                else:
                    doubleDouble=True

            if(x==secondPrevious):
                repeatAfterOne=True

            if(previous!=None):
               secondPrevious=previous

            previous=x

        if( doubleDouble and repeatAfterOne):
            count+=1
    else:
        break
print(count)
