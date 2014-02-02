import time
import os


def clear():
	os.system("cls" if os.name == "nt" else "clear")


class UI(object):

	def __init__(self, delay):
		self.__delay = delay

	def display(self, board):
		clear()

		for row in board:
			tmp_row = []

			for state in row:
				if state == 0:
					tmp_row.append("_")
				else:
					tmp_row.append("1")

			print("".join(tmp_row))

		time.sleep(self.__delay)