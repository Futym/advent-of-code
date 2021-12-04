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
                    tab[boardIndex][rowIndex][itemindex]=-1
    for board in tab:
        for row in board:
            if  row==[-1,-1,-1,-1,-1]:
                if(len(tab)==1):
                    winPoints=countPoints(board,number)
                else:
                    tab.remove(board)
                break
            if(board[0][itemindex]==board[1][itemindex]==board[2][itemindex]==board[3][itemindex]==board[4][itemindex]==-1):
                if(len(tab)==1):
                    winPoints=countPoints(board,number)
                else:
                    tab.remove(board)
                break
        
        if(winPoints!=0):
            break
    if(winPoints!=0):
        break

                    

print(winPoints)      
                       




    