from random import shuffle
import copy

class main:

    def __init__(self, grid = None):
        self.counter = 0
        # Path is for the matplotlib animation
        self.path = []
        # If a grid/puzzle is passed in, make a copy to solve
        if grid:
            if len(grid[0]) == 9 and len(grid) == 9:
                self.grid = grid
                self.original = copy.deepcopy(grid)
                self.solve_input_sudoku()
            else:
                print("Input needs to be a 9x9 matrix")
        else:
            # If not puzzle is passed then one is generated
            self.grid = [[0 for i in range(9)] for j in range(9)]
            self.generate_puzzle()
            self.original = copy.deepcopy(self.grid)

def generate_puzzle(self):
    """ Generates new puzzle and solves it """
    self.generate_solution(self.grid)
    self.print_grid('Full solution')
    self.remove_numbers_from_grid()
    self.print_grid("With remove numbers")
    return

def print_grid(self, grid_name = None):
    if grid_name:
        print(grid_name)
    for row in self.grid:
        print(row)
    return

def generate_solution(self, grid):
    """ Generates a full solution using backtracking"""
    number_list = [1,2,3,4,5,6,7,8,9]
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        # Find the next empty #
        if grid[row][col] == 0:
            shuffle(number_list)
            for number in number_list:
                if self.valid_location(grid, row, col, number):
                    self.path.append((number, row, col))
                    grid[row][col] = number
                    if not self.find_empty_square(grid):
                        return True
                    else:
                        if self.generate_solution(grid):
                            # If the grid is full
                            return True
            break
    grid[row][col] = 0
    return False