import sys

chessboard = []
for index in range(8):
    chessboard.append(list(sys.stdin.readline().strip()))

num_queens = 0
valid = True
for row in range(8):
    for column in range(8):
        if chessboard[row][column] == '*':
            num_queens += 1

if num_queens != 8:
    valid = False

rowValid = True
#checking rows
for row in range(8):
    numberOfQueens = 0
    for column in range(8):
        if chessboard[row][column] == "*":
            numberOfQueens += 1
    if numberOfQueens > 1:
        rowValid = False

columnValid = True      
for column in range(8):
    numberOfQueens = 0
    for row in range(8):
        if chessboard[row][column] == "*":
            numberOfQueens += 1
    
    if numberOfQueens > 1:
        columnValid = False

diagonalValid = True
for i in range(8):
    for j in range(8):
        if (chessboard[i][j] == "*"): 
            for k in range(8):
                for l in range(8):
                    if ((abs(i - k) == abs(j - l)) and chessboard[k][l] == "*" and (k != i or l != j)):
                            diagonalValid = False
    
if (not valid):
    print("Invalid")
elif (diagonalValid and columnValid and rowValid):
    print("Valid")
elif (not diagonalValid or not columnValid or not rowValid):
    print("Invalid")