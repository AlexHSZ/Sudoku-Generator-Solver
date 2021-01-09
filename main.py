board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(self):

    find = find_empty(self)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if valid(self, i, (row, col)):
            self[row][col] = i
            
            if solve(self):
                return True
            
            self[row][col] = 0

    return False

def valid(self, num, pos):
    # Check row
    for i in range(len(self[0])):
        if self[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(self)):
        if self[i][pos[1]] == num and pos[0] != i:
            return False

    # Check subgrid
    subX = pos[1] // 3
    subY = pos[0] // 3

    for i in range(subY * 3, subY * 3 + 3):
        for j in range(subX * 3, subX * 3 + 3):
            if self[i][j] == num and (i, j) != pos:
                return False

    return True

def print_board(self):
    for i in range(len(self)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(self[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(self[i][j])
            else:
                print(str(self[i][j]) + " ", end="")

def find_empty(self):
    for i in range(len(self)):
        for j in range(len(self[0])):
            if self[i][j] == 0:
                return (i, j) # Tuple of row, col

print_board(board)
solve(board)
print(" ============================== ")
print_board(board)

