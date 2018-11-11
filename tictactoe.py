def intructions():
    """Display game instructions."""  
    print(
    """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.  
    This will be a showdown between your human brain and my silicon processor.  

    You will make your move known by entering a number, 0 - 8.  The number 
    will correspond to the board position as illustrated:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    Prepare yourself, human.  The ultimate battle is about to begin. \n\n\n
    """
    )
def firstmove():
    response=None
    while response not in ("y","n"):
        response=input("Do you want first move?(y/n):")
    if response == "y":
        human=X
        computer=O
    else:
        human=O
        computer=X
    return computer,human
def newboard():
    board=[]
    for i in range(BOX):
        board.append(EMPTY)
    return board
def displayboard(board):
    print("\n\t",board[0],"| ",board[1]," | ",board[2])
    print("\t","------------")
    #print("\t"," ","| "," "," |"," ")
    print("\n\t",board[3],"| ",board[4]," | ",board[5])
    print("\t","------------")
    #print("\t"," ","| "," "," |"," ")
    print("\n\t",board[6],"| ",board[7]," | ",board[8])
def legalmoves(board):
    moves=[]
    for ink in range(BOX):
        if board[ink]==EMPTY:
            moves.append(ink)
    return moves
def humanmove(board):
    print("-----------------------------")
    legal=legalmoves(board)
    place=None
    while place not in legal:
        place=int(input("Where you wanna to move: "))
        if place not in legal:
            print("Hey, Foolish human. That place is already occupied, take another place.")   
    return place
def computermove(board):
    legal=legalmoves(board)
    BESTMOVES=(4,0,2,6,8,1,3,5,7)
    #checking any next step is winning for computer, if yes take that step
    for i in legal:
        board[i]=computer
        if winner(board)==computer:
            print("I choose ",i)
            return int(i)
        board[i]=EMPTY
    #checking any next step is winning for human, if yes take that step
    for i in legal:
        board[i]=human
        if winner(board)==human:
            print("I choose ",i)
            return int(i)
        board[i]=EMPTY
    #next step is not a winning step
    for i in BESTMOVES:
        for i in legal:
            print("\nI choose ",i)
            return int(i)
def winner(board):
    win=None
    WAYSTOWIN=((0,1,2),(2,5,8),(6,7,8),(0,3,6),(1,4,7),(3,4,5),(0,4,8),(2,4,6))
    for row in WAYSTOWIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            win=board[row[0]]
            return win
    if EMPTY not in board:
        return Tie
def nextturn(turn):
    if turn == X:
        turn=O
    else:
        turn=X
    return turn
def congratswinner(w):
    if w == human:
         print("No no, how this was happened?? it is not possible. how a human can beat a silicon processor, im superior than humans. :'( I think this will happened in flook")
    elif w == computer:
        print("Haha, ROFL. A human can never ever beat a computer. We are superior than human beings. Poda thontangoli Haha")
    else:
        print("Appada, It's a tie.. It's a nail biting finish.")
#Main
X="X"
O="O"
Tie="TIE"
EMPTY=" "
BOX=9
intructions()
computer,human=firstmove()
turn=X
board=newboard()
displayboard(board)
while not winner(board):
    if turn == human:
        move=humanmove(board)
        board[move]=human
    else:
        move=computermove(board)
        board[move]=computer
    displayboard(board)
    turn=nextturn(turn)
congratswinner(winner(board))
input("Press any key to exit")
