# Welcome to our game Board
import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
firstPlayer = "X"
winner = None
gameRunning = True


# The game board
def printBoard(board):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("---------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("---------")
        print(board[6] + " | " + board[7] + " | " + board[8])
printBoard(board)

# Define player

def playerInput(board):
        num = int(input("Enter a number between 1 to 9 "))
        if num >= 1 and num <= 9 and board[num-1] == "-":
                board[num-1] = firstPlayer
        else:
                print("Oops that place is already used!")

# Define position of the number inside the board

def checkPosition(board):
        global winner
        if board[0] == board [1] == board[2] and board[1] != "-":
                winner = board[0]
                return True
        elif board[3] == board [4] == board[5] and board[3] != "-":
                winner = board[3]
                return True
        elif board[6] == board [7] == board[8] and board[6] != "-":
                winner = board[6]
                return True
def checkRow(board):
        global winner
        if board[0] == board[3] == board[6] and board[0] != "-":
                winner = board[0]
                return True
        elif board[1] == board[4] == board[7] and board[1] != "-":
                winner = board[1]
                return True
        elif board[2] == board[5] == board[8] and board[2] != "-":
                winner = board[2]
                return True

def checkDiagonal(board):
        global winner
        if board[0] == board[4] == board[8] and board[0] != "-":
                winner = board[0]
                return True
        elif board[2] == board[4] == board[6] and board[2] != "-":
                winner = board[2]
                return True

def checkTie(board):
        if "-" not in board:
            printBoard(board)
            print("Try again!")
            gameRunning = False

# Define who is the winner

def checkWin():
        if checkDiagonal(board) or checkRow(board) or checkPosition(board):
                print(f"The winner is  {winner}")

# Define who is going to play

def switchPlayer():
        global firstPlayer
        if firstPlayer == "X":
           firstPlayer = "O"
        else:
           firstPlayer = "X"

# Define computer Board

def computer(board):
        while firstPlayer == "O":
            position = random.randint(0, 8)
            if board[position] == "-":
                    board[position] == "O"
                    switchPlayer()

# Define condition of the running game if we have a winner or we have to restart

while gameRunning:
        printBoard(board)
        playerInput(board)
        checkWin()
        checkTie(board)
        switchPlayer()
        computer(board)
        checkWin()
        checkTie(board)