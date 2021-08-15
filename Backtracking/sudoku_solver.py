def input_board():
    board = [[0 for c in range(9)] for r in range(9)] 
    for i in range(0, 9):
        for j in range(0, 9):
            board[i][j] = int(input('Enter the element at ' + str(i + 1) + ' row and ' + str(j + 1) + ' column')) 
    return board

def valid(b, num, pos):
    # check row
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # loop through all 9 elements in the box
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(b):
    find = find_empty_slot(b)
    if not find:
        return True

    else:
        row, col = find

    for x in range(1, 10):  # trying numbers from 1 to 9 to see if it fits in the empty slot
        if valid(b, x, (row, col)):
            b[row][col] = x

            if solve(b):
                return True

            b[row][col] = 0

    return False


def print_board(b):
    ''' Print the board with separations '''

    for i in range(len(b)):
        if i % 3 == 0 and i != 0:  # print a horizontal line after every third row
            print("--------------------------")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0: 
                print(" | ", end="")  # print a '|' after every third element 

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="") # go to the next line at the end of the row

def find_empty_slot(b):
    ''' Find an empty slot across the board '''

    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j) 
    return None

board = input_board()
print_board(board)
print("")
solve(board)
print("")
print_board(board)
