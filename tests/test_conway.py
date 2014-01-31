import unittest
import conway


class ConwayTest(unittest.TestCase):
	def test_get_new_state(self):
		"""
		Test the program's ability to determine the next cell state
		"""
		# Format of tuples: (state, neighbors, output)
		input_combinations = [
			(1, 0, 0), (1, 1, 0), (1, 2, 1), (1, 3, 1), (1, 4, 0), (1, 5, 0), (1, 6, 0), (1, 7, 0), (1, 8, 0),
			(0, 0, 0), (0, 1, 0), (0, 2, 0), (0, 3, 1), (0, 4, 0), (0, 5, 0), (0, 6, 0), (0, 7, 0), (0, 8, 0),
		]

		for i in input_combinations:
			self.assertEqual(
				conway.get_new_state(i[0], i[1]),
				i[2],
				"Failed on: Cell={0[0]}, Neighbors={0[1]}, Output={0[2]}".format(i)
			)

	def test_get_board_from_path(self):
		"""
		Test whether the program is correctly reading text files that represent the starting board
		"""
		board = conway.get_board_from_file('test_board_2x2.txt')
		mock_board = [
			[0, 0],
			[1, 0]
		]
		self.assertEqual(board, mock_board)

	def test_game_live(self):
		"""
		Test whether the program is able to survive a generation
		"""
		mock_board = [
			[0, 0],
			[1, 0]
		]
		game = conway.Game(mock_board)
		game.live(1)
		self.assertTrue(True)


if __name__ == '__main__':
	unittest.main()