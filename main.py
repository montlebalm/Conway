#!/usr/bin/env python

import conway
import simple_ui
import sys

if __name__ == "__main__":
	# Pull in the command line args
	path = sys.argv[1]
	iterations = int(sys.argv[2])

	# Get the board from the specified file
	raw_seed_board = [list(line.strip()) for line in open(path)]
	starting_board = [list(map(int, line)) for line in raw_seed_board]

	# Start the game
	ui = simple_ui.UI(.1)
	game = conway.Game(starting_board, ui.display)
	game.live(iterations)