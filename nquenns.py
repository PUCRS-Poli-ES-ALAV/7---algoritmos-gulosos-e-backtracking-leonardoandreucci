line = [0 for _ in range(7)]
table = [line for _ in range(7)]
"""
The idea is to use backtracking to check all possible combinations of n queens in a chessboard of order n*n. To do so, first create an auxiliary matrix mat[][] of order n*n to mark the cellsoccupied by queens. Start from the first row and for each row  place queen at different columns and check for clashes with other queens. To check for clashes, iterate through all the rows of current column and both the diagonals. If it is safe to place queen in current column, mark the cell occupied in matrix mat[][] and move to the next row. If at any row, there is no safe column to place the queen, backtrack to previous row and place the queen in other safe column and again check for the next row.
"""


def print_table():
    for l in table:
        print(l)

def is_safe(x, y):
    # linha
    l_local = table[x]
    for i in range(len(l_local)):
        if l_local[i] == 1:
            return False

    # coluna
    col = y
    for j in range(len(line)):
        if table[j][col] == 1:
            return False

    # diagonais
    for i in range(x, len(line)):
        for j in range(y, len(line)):
            table
