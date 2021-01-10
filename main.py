from random import shuffle
import copy

board1 = [
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

class SudokuGenerator:

	def __init__(self, board = None):
		self.counter = 0
		# If a board has been passed in, make a copy to solve
		if board:
			print("To implement")
		else:
			# If no board is passed in, generate one
			self.board = [[0 for i in range(9)] for j in range(9)]
			self.generate_board()
			self.original = copy.deepcopy(self.board)

	def generate_board(self):
		# Generates a new board and solves it
		self.generate_solution()
		self.print_board(self.board)

	def num_used_in_row(self, row, num):
		if num in self.board[row]:
			return True
		return False
	
	def num_used_in_col(self, col, num):
		for i in range(9):
			if self.board[i][col] == num:
				return True
		return False

	def num_used_in_subgrid(self, row, col, num):
		subX = (row // 3) * 3
		subY = (col // 3) * 3

		for i in range(subX, (subX + 3)):
			for j in range(subY, (subY + 3)):
				if self.board[i][j] == num:
					return True
		return False

	def valid_location(self, row, col, num):
		if self.num_used_in_row(row, num):
			return False
		elif self.num_used_in_col(col, num):
			return False
		elif self.num_used_in_subgrid(row, col, num):
			return False
		return True

	def find_empty(self):
		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				if self.board[i][j] == 0:
					return (i, j) # Tuple of row, col
		return

	def generate_solution(self):
		number_list = [1,2,3,4,5,6,7,8,9]
		for i in range(0, 81):
			row = i // 9
			col = i % 9
			# Find the next cell 
			if self.board[row][col] == 0:
				shuffle(number_list)
				for number in number_list:
					if self.valid_location(row, col, number):
						self.board[row][col] = number
						if not self.find_empty():
							return True
						else:
							if self.generate_solution():
								# If the board is full
								return True
				break
		self.board[row][col] = 0
		return False

	def print_board(self, board):
		for i in range(len(board)):
			if i % 3 == 0 and i != 0:
				print("- - - - - - - - - - - -")
		
			for j in range(len(board[0])):
				if j % 3 == 0 and j != 0:
					print(" | ", end="")

				if j == 8:
					print(board[i][j])
				else:
					print(str(board[i][j]) + " ", end="")

new_board = SudokuGenerator()

# def solve(self):

# 	find = find_empty(self)
# 	if not find:
# 		return True
# 	else:
# 		row, col = find

# 	for i in range(1, 10):
# 		if valid(self, i, (row, col)):
# 			self[row][col] = i

# 			if solve(self):
# 				return True
		
# 			self[row][col] = 0

# 	return False

# def valid(self, num, pos):
# 	# Check row
# 	for i in range(len(self[0])):
# 		if self[pos[0]][i] == num and pos[1] != i:
# 			return False

# 	# Check column
# 	for i in range(len(self)):
# 		if self[i][pos[1]] == num and pos[0] != i:
# 			return False

# 	# Check subgrid
# 	subX = (pos[1] // 3) * 3
# 	subY = (pos[0] // 3) * 3

# 	for i in range(0, 3):
# 		for j in range(0, 3):
# 			if self[subY + i][subX + j] == num:
# 				return False

# 	return True

# def print_board(self):
# 	for i in range(len(self)):
# 		if i % 3 == 0 and i != 0:
# 			print("- - - - - - - - - - - -")
	
# 		for j in range(len(self[0])):
# 			if j % 3 == 0 and j != 0:
# 				print(" | ", end="")

# 			if j == 8:
# 				print(self[i][j])
# 			else:
# 				print(str(self[i][j]) + " ", end="")

# def find_empty(self):
# 	for i in range(len(self)):
# 		for j in range(len(self[0])):
# 			if self[i][j] == 0:
# 				return (i, j) # Tuple of row, col
# 	return
		
# print_board(board)
# solve(board)
# print(" ============================== ")
# print_board(board)



