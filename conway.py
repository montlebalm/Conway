#!/usr/bin/env python

import time


def display_board(title, board, delay):
	print(title)
	for row in board:
		print("".join(map(str, row)))
	print()
	time.sleep(delay)


def determine_state(cell, num_neighbors):
	"""
	Determine the cell's fate based on the following rules:
	- Any live cell with fewer than two live neighbours dies, as if caused by under-population.
	- Any live cell with two or three live neighbours lives on to the next generation.
	- Any live cell with more than three live neighbours dies, as if by overcrowding.
	- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
	"""
	if cell == 1:
		if num_neighbors > 3 or num_neighbors < 2:
			return 0
		else:
			return 1
	elif num_neighbors == 3:
		return 1
	else:
		return cell


class Game(object):
	def __init__(self, board):
		self._board = board
		self._height = len(self._board)
		self._width = len(self._board[0])

	def live(self, iterations):
		display_board("Beginning", self._board, 0)

		for generation in range(0, iterations):
			self.iterate(generation + 1)

	def get_cell_state(self, y, x):
		if 0 <= y <= self._height - 1:
			if 0 <= x <= self._width - 1:
				return self._board[y][x]
		return 0

	def iterate(self, generation):
		"""
		Play out 1 generation
		"""
		next_board = []

		for y, row in enumerate(self._board):
			next_board.append([])

			for x, cell in enumerate(row):
				neighbors = [
					self.get_cell_state(y - 1, x - 1),
					self.get_cell_state(y - 1, x),
					self.get_cell_state(y - 1, x + 1),
					self.get_cell_state(y, x - 1),
					self.get_cell_state(y, x + 1),
					self.get_cell_state(y + 1, x - 1),
					self.get_cell_state(y + 1, x),
					self.get_cell_state(y + 1, x + 1)
				]
				num_neighbors = sum(neighbors)
				state = determine_state(cell, num_neighbors)
				next_board[y].append(state)

		self._board = next_board
		display_board("Generation " + str(generation), self._board, .5)

# Start the game
raw_seed_board = [list(line.strip()) for line in open("seed.txt")]
seed_board = [list(map(int, line)) for line in raw_seed_board]
game = Game(seed_board)
game.live(10)