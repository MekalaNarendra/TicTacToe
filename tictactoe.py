board = [" " for x in range(10)]

def insertletter(letter,pos):
    board[pos]=letter

def isspacefree(pos):
    return board[pos]==" "

def printboard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def iswinner(bo,le):
    return(bo[7]==le and bo[8]==le and bo[9]==le)or (bo[4]==le and bo[5]==le and bo[6]==le)or (bo[1]==le and bo[2]==le and bo[3]==le)or (bo[1]==le and bo[4]==le and bo[7]==le)or (bo[2]==le and bo[5]==le and bo[8]==le)or (bo[3]==le and bo[6]==le and bo[9]==le)or (bo[1]==le and bo[5]==le and bo[9]==le)or (bo[3]==le and bo[5]==le and bo[7]==le)

def playermove():
    run = True
    move=input("select any postition to insert \'X\' in (1-9):  ")
    try:
        move=int(move)
        if move>0 and move<10:
            if isspacefree(move):
                run=False
                insertletter("X",move)
            else:
                print("sorry ! , space is already occupied")
        else:
            print("enter number in between the range 1 to 9")
    except:
        print("only numbers are allowed")

def computermove():
    possiblemoves = [x for x, letter in enumerate(board) if letter == " " and x!=0]
    move = 0

    for let in ["O","X"]:
        for i in possiblemoves:
            boardcopy=board[:]
            boardcopy[i]=let
            if iswinner(boardcopy,let):
                move=i
                return move

    cornersopen=[]
    for i in possiblemoves:
        if i in [1,3,7,9]:
            cornersopen.append(i)
            
    if len(cornersopen) > 0:
        move = selectrandom(cornersopen)
        return move

    if 5 in possiblemoves:
        move = 5
        return move

    
    edgesopen=[]
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edgesopen.append(i)
            
    if len(edgesopen) > 0:
        move = selectrandom(edgesopen)
        
    return move
        

def selectrandom(li):
    import random
    ln=len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isboardfull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

def main():
    print("welcome to the game TIC TAC TOE")
    printboard(board)

    while not (isboardfull(board)):
        if not (iswinner(board,"O")):
            playermove()
            printboard(board)
        else:
            print("oops !,better luck next time computer won")
            break

        if not (iswinner(board,"X")):
            move = computermove()
            if move == 0:
                print("Tie Game!")
            else:
                insertletter("O",move)
                print("computer placed the letter 'O' in position",move)
                printboard(board)
        else:
            print("congratulations, you won this time good job")
            break

    if isboardfull(board):
        print("game is tied")


count=1
while True:
    answer = input('Do you want to play (Y/N)')
    print("\n")
    print(" remember only 10 chances are")
    print("\n")
    try:
        if answer.lower() == 'y' or answer.lower == 'yes':
            print("chance number",count)
            board = [' ' for x in range(10)]
            print('-----------------------------------')
            main()
            print("no of times played",count)
            count=count+1
            if count > 10:
                print("you played 10 times so no more chances to play")
                exit()
    except:
        print("enter only y or n")
    try:
        if answer.lower() == "n" or answer.lower=="no":
            exit()
    except:
        print("enter only y or n")
    
    
    
               
    
    
