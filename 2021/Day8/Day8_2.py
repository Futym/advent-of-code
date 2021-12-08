file=open("Day8/Day8.txt")
count=0
index=0
tab=["" for x in range(0,10)]
while True:
    temp=file.readline()
    if temp:
        number=""
        temp=temp.replace(" | "," ").split()
        print(temp)
        for x in range(0,10):
            if(len(temp[x])==2):
                tab[1]=temp[x]
            if(len(temp[x])==3):
                tab[7]=temp[x]
            if(len(temp[x])==4):
                tab[4]=temp[x]
            if(len(temp[x])==7):
                tab[8]=temp[x]
        for x in range(0,10):
            if(len(temp[x])==6):
                flagNine=True
                flagSix=False
                for item in tab[4]:
                    if item in temp[x]:
                        pass
                    else:
                        flagNine=False
                for item in tab[1]:
                    if item in temp[x]:
                        pass
                    else:
                        flagSix=True

                if(flagNine):
                    tab[9]=temp[x]
                elif(flagSix):
                    tab[6]=temp[x]
                else:
                    tab[0]=temp[x]


            if(len(temp[x])==5):
                flagFive=0
                flagThree=True
                for item in tab[4]:
                    if item in temp[x]:
                        pass
                    else:
                        flagFive+=1
                for item in tab[1]:
                    if item in temp[x]:
                        pass
                    else:
                        flagThree=False
                if(flagThree):
                    tab[3]=temp[x]
                elif(flagFive==1):
                    tab[5]=temp[x]
                else:
                    tab[2]=temp[x]
        for x in range(10,14):
            if(len(temp[x])==2):
                count=1
            elif(len(temp[x])==3):
                count=7
            elif(len(temp[x])==4):
                count=4
            elif(len(temp[x])==7):
                count=8

            else:
                twoFlag=True
                fiveFlag=True
                if(len(temp[x])==5):
                    for i in tab[2]:
                        if(i in temp[x]):
                            pass
                        else:
                            twoFlag=False
                    for i in tab[5]:
                        if(i in temp[x]):
                            pass
                        else:
                            fiveFlag=False
                    if(twoFlag):
                        count=2
                    elif(fiveFlag):
                        count=5
                    else:
                        count=3
                nineFlag=True
                sixFlag=True
                if(len(temp[x])==6):
                    for i in tab[9]:
                        if(i in temp[x]):
                            pass
                        else:
                            nineFlag=False
                    for i in tab[6]:
                        if(i in temp[x]):
                            pass
                        else:
                            sixFlag=False
                    if(nineFlag):
                        count=9
                    elif(sixFlag):
                        count=6
                    else:
                        count=0
            number+=str(count)
        print (tab)
        print(number)
        index+=int(number)
                
            
    else:
        break
print (index)