import random
board = [
    "-","-","-",
    "-","-","-",
    "-","-","-"
]

CurrentPlayer = "X"
is_gameRunning = True
winner = None

# Function for printing the board

def PrintBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("------------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("------------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Function for user playing
def PlayerInput(board):
    inp = int(input("Enter the position from 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = CurrentPlayer
    else:
        print("The spot is taken or invalid")
        PlayerInput(board)

# Function for checking for a win or a tie
# Checking for a horizontal win
def CheckHor(board):
    global winner
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]
        return True

# Checking for a vertical win
def CheckVer(board):
    global winner
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] != "-":
        winner = board[2]
        return True

# Checking for a diagonal win
def CheckDia(board):
    global winner
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] != "-":
        winner = board[2]
        return True

# Checking for a tie
def CheckTie(board):
    global is_gameRunning
    if "-" not in board:
        is_gameRunning = False
        print("It's a tie")

#Checking for the game winner
def CheckWin(board):
    if CheckHor(board) or CheckVer(board) or CheckDia(board):
        global is_gameRunning
        is_gameRunning = False
        PrintBoard(board)
        print(f"The winner is {winner}")
        

# For switching the players
def SwitchPlayer():
    global CurrentPlayer
    if CurrentPlayer == "X":
        CurrentPlayer = "O"
    else:
        CurrentPlayer = "X"

# For using a computer player
def ComputerPlayer(board):
    global CurrentPlayer
    while CurrentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            SwitchPlayer()
# For playing the game
while is_gameRunning:
    PrintBoard(board)
    PlayerInput(board)
    CheckHor(board)
    CheckVer(board)
    CheckDia(board)
    CheckTie(board)
    CheckWin(board)
    SwitchPlayer()
    ComputerPlayer(board)

# End of the game