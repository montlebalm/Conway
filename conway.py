def get_new_state(state, num_neighbors):
	"""
	Determine the cell's fate based on the following rules:
	- Any live cell with fewer than two live neighbours dies, as if caused by under-population.
	- Any live cell with two or three live neighbours lives on to the next generation.
	- Any live cell with more than three live neighbours dies, as if by overcrowding.
	- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
	"""
	if state == 1:
		if num_neighbors > 3 or num_neighbors < 2:
			return 0
		else:
			return 1
	elif num_neighbors == 3:
		return 1
	else:
		return state


class Game(object):
	def __init__(self, board, display):
		if board and len(board):
			self.__board = board
			self.__display = display
			self.__height = len(self.__board)
			self.__width = len(self.__board[0])

	def live(self, iterations):
		self.__display(self.__board)

		while iterations > 0:
			self.__iterate()
			iterations -= 1

	def __get_cell_state(self, y, x):
		"""
		Get the cell state for the given x, y coordinate
		"""
		if 0 <= y <= self.__height - 1:
			if 0 <= x <= self.__width - 1:
				return self.__board[y][x]
		return 0

	def __iterate(self):
		"""
		Play out 1 generation
		"""
		next_board = []

		for y, row in enumerate(self.__board):
			next_board.append([])

			for x, cell in enumerate(row):
				neighbors = [
					self.__get_cell_state(y - 1, x - 1),
					self.__get_cell_state(y - 1, x),
					self.__get_cell_state(y - 1, x + 1),
					self.__get_cell_state(y, x - 1),
					self.__get_cell_state(y, x + 1),
					self.__get_cell_state(y + 1, x - 1),
					self.__get_cell_state(y + 1, x),
					self.__get_cell_state(y + 1, x + 1)
				]
				num_neighbors = sum(neighbors)
				state = get_new_state(cell, num_neighbors)
				next_board[y].append(state)

		self.__board = next_board
		self.__display(self.__board)