def countPoints(board, number):
    sum=0
    for row in board:
        for item in row:
            if(item!=-1):
                sum+=int(item)
    sum*=int(number)
    return sum


file=open("Day4/Day4.txt")
numbers=file.readline().split(",")
print (numbers)
tab=[]
winPoints=0
while(True):
    test=file.readline()
    if(test):
        board=[]
        for x in range(0,5):
            pom=file.readline().split()
            board.append(pom)
        tab.append(board)
    else:
        break
for number in numbers:
    for board in tab:
        for row in board:
            for item in row:
                if(item==number):
                    itemindex=row.index(item)
                    rowIndex=board.index(row)
                    boardIndex=tab.index(board)
                    print(tab[boardIndex][rowIndex][itemindex])
                    tab[boardIndex][rowIndex][itemindex]=-1
                    print(tab[boardIndex][rowIndex][itemindex])
                    print(item)
                    print(board)
                    print(tab[boardIndex])

                    if  row==[-1,-1,-1,-1,-1]:
                        winPoints=countPoints(board,number)
                        break
                    if(board[0][itemindex]==board[1][itemindex]==board[2][itemindex]==board[3][itemindex]==board[4][itemindex]==-1):
                        winPoints=countPoints(board,number)
                        break
            if(winPoints!=0):
                break
        if(winPoints!=0):
            break
    if(winPoints!=0):
        break

                    

print(winPoints)      
                       




    