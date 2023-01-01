gameBoard = [' ' for x in range(10)]


def insertSymbol(pos, symbol):
    gameBoard[pos] = symbol


def spaceIsFree(pos):
    return gameBoard[pos] == ' '


def printBoard(gameBoard):
    print('   |   |')
    print(' ' + gameBoard[1] + ' | ' + gameBoard[2] + ' | ' + gameBoard[3])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + gameBoard[4] + ' | ' + gameBoard[5] + ' | ' + gameBoard[6])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + gameBoard[7] + ' | ' + gameBoard[8] + ' | ' + gameBoard[9])
    print('   |   |')


def checkWinner(bo,le):
    return (bo[1]==le and bo[2] == le and bo[3]==le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5]== le and bo[7] == le)


def playerMove():
    run=True
    while run:
        move=input('Enter your position b/w (1-9)')
        try:
            move=int(move)
            if move>0 and move<10:
                if spaceIsFree(move):
                    run=False
                    insertSymbol(move,'X')
                else:
                    print('This place is already taken! Choose Another')
            else:
                print('Position out of range! please insert b/w (1-9)')
        except:
            print('Please enter a Integer value')


def compMove():
    possibleMoves = [x for x,symbol in enumerate(gameBoard) if symbol==' ' and x != 'O']
    move=0
    for sym in ['O','X']:
        for i in possibleMoves:
            boardCopy = gameBoard[:]
            boardCopy[i]=sym
            if checkWinner(boardCopy,sym):
                move=i
                return move

    cornersOpen=[]
    for i in possibleMoves:
        if i in (1,3,7,9):
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move=selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move=5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in (2,4,6,8):
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln=len(li)
    r=random.randrange(ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print('Welcome Tic Tac Toe')
    printBoard(gameBoard)

    while not(isBoardFull(gameBoard)):
        if not(checkWinner(gameBoard,'O')):
            playerMove()
            printBoard(gameBoard)
        else:
            print('Sorry, O\'s has won this time!')
            break
        if not(checkWinner(gameBoard,'X')):
            move = compMove()
            if move==0:
                print('This is a Tie! Try Again')
            else:
                insertSymbol(move,'O')
                print('CPU has played it\'s turn at',move, ':' )
                printBoard(gameBoard)
        else:
            print('Congratulations, X\'s won this time!')
            break


while True:
    play=int(input('Press 1 to play 0 to exit :'))
    if play==1:
        main()
    else:
        exit()