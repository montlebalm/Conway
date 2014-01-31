#!/usr/bin/env python

import time


def display_board(title, board, delay):
	print(title)
	for row in board:
		print("".join(map(str, row)))
	print()
	time.sleep(delay)


def get_board_from_file(path):
	raw_seed_board = [list(line.strip()) for line in open(path)]
	return [list(map(int, line)) for line in raw_seed_board]


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
	def __init__(self, board):
		if board and len(board):
			self.__board = board
			self.__height = len(self.__board)
			self.__width = len(self.__board[0])

	def live(self, iterations):
		display_board("Beginning", self.__board, 0)

		for generation in range(0, iterations):
			self.__iterate(generation + 1)

	def __get_cell_state(self, y, x):
		if 0 <= y <= self.__height - 1:
			if 0 <= x <= self.__width - 1:
				return self.__board[y][x]
		return 0

	def __iterate(self, generation):
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
		display_board("Generation " + str(generation), self.__board, .5)

if __name__ == '__main__':
	starting_board = get_board_from_file('seed.txt')
	game = Game(starting_board)
	game.live(10)