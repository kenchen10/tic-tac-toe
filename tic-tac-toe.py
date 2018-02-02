"""I made this game of tic-tac-toe."""
p1 = 1
p2 = 2
def createBoard(size):
    #Creates a board of size x size dimensions.
    board = [[None for i in range(size)] for j in range(size)]
    return board

def getLoc():
    #Gets user input for where to put piece.
    print("What x position do you want to put your piece?")
    x = int(input())
    print("What y position do you want to put your piece?")
    y = int(input())
    return x, y

def isOver(board, player):
    #Determines whether the game is over.
    if isThree(board, player): #If there is three in a row, game over.
        return True
    if isFull(board): #If the board is full, game over.
        return True
    return False

def isFull(board):
    #Checks if the board is full.
    for row in board:
        if None in row: #If there is an empty space, the board isn't full.
            return False
    return True

def isThree(board, player):
    #Checks if there is three in a row
    if player == p1:
        piece = "x"
    else:
        piece = "o"
    #Check if there are 3 in a row.
    for row in range(len(board)):
        for c in range(len(board)):
            if board[row][c] != piece:
                break
            elif board[row][c] == piece and c == len(board) - 1:
                print("Player" + str(player) + " has won!")
                return True
    #Check if there are 3 in a column.
    for col in range(len(board)):
        for r in range(len(board)):
            if board[r][col] != piece:
                break
            elif board[r][col] == piece and r == len(board) - 1:
                print("Player" + str(player) + " has won!")
                return True
    #Check if there are 3 in a diagonal.
    for i in range(len(board)):
        #Down and to the right diagonal.
        if board[i][i] != piece:
            break
        if board[i][i] == piece and i == len(board) - 1:
            print("Player" + str(player) + " has won!")
            return True
    for i in range(len(board)):
        #Up and to the right diagonal.
        if board[i][len(board) - 1 - i] != piece:
            break
        if board[i][len(board) - 1 -i] == piece and i == len(board) - 1:
            print("Player" + str(player) + " has won!")
            return True
    return False

def putPiece(piece, board):
    #Places piece at board[x][y].
    x, y = getLoc()
    if board[x][y] != None: #Check if there is already a piece there.
        print("There is alreay a piece there, choose again.")
        return putPiece(piece, board)
    board[x][y] = piece

def takeTurn(player, board):
    #Simulates a turn of tic-tac-toe.
    if player == p1:
        putPiece("x", board)
    else:
        putPiece("o", board)

def play():
    #Simulates a game.
    board = createBoard(3) #Create a board.
    over = False
    while over != True: #Keep going until game is over.
        takeTurn(p1, board)
        print(board)
        over = isOver(board, p1)
        if over == True:
            break
        takeTurn(p2, board)
        print(board)
        over = isOver(board, p2)
