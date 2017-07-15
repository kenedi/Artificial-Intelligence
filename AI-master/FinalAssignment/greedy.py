
from minimax import *


class Greedy(Minimax):
	""" alphabeta object that takes a current connect four"""
	timeLimit = 0
	boardScores = [[3,4,5,7,5,4,3],[4,6,8,10,8,6,4],[5,8,11,13,11,8,5],[5,8,11,13,11,8,5],[4,6,8,10,8,6,4],[3,4,5,7,5,4,3]]

	def __init__(self, board):
		#copy the board
		super(Greedy, self).__init__(board)

	def best_move(self, state, curr_player):
		""" Returns the best move (as a column number) and the associated alpha
		Calls search()
		"""
		# determine opponent's color
		if curr_player == self.colors[0]:
			opp_player = self.colors[1]
		else:
			opp_player = self.colors[0]

		return self.value(state, curr_player)



	def value(self, state, symbol):
		moves = self.boardScores[1]
		for col in range (7):
			for row in range(6):
				if state[row][col] == " ":
					moves[col] = self.returnScore(state, row, col, self.boardScores[row][col])
					break
				elif row ==5:
					moves[col] = -1
					break
		# print("Column scores: ", moves)
		return moves.index(max(moves))


	def returnScore(self, state, row, col, score):
		# print("CHECKING ROW: ", row)

		if self.boardSpot(state, row+1, col-1) == 'x':
				if self.boardSpot(state, row+2, col-2) == 'x' or self.boardSpot(state, row-1, col+1) == 'x':
					if self.boardSpot(state, row+3, col-3) == 'x' or self.boardSpot(state, row-1, col+1) == 'x':
						score = score * 100000
					score = score * 60
				score = score + 1
		elif self.boardSpot(state, row+1, col-1) == 'o':
				if self.boardSpot(state, row+2, col-2) == 'o' or self.boardSpot(state, row-1, col+1) == 'o':
					if self.boardSpot(state, row+3, col-3) == 'o' or self.boardSpot(state, row-1, col+1) == 'o':
						score = score * 10000000000000
					score = score * 500
				score = score * 2

		if self.boardSpot(state, row, col-1) == 'x':
				if self.boardSpot(state, row, col-2) == 'x' or self.boardSpot(state, row, col+1) == 'x':
					if self.boardSpot(state, row, col-3) == 'x' or self.boardSpot(state, row, col+1) == 'x':
						score = score * 100000
					score = score * 60
				score = score + 1

		elif self.boardSpot(state, row, col-1) == 'o':
				if self.boardSpot(state, row, col-2) == 'o' or self.boardSpot(state, row, col+1) == 'o':
					if self.boardSpot(state, row, col-3) == 'o' or self.boardSpot(state, row, col+1) == 'o':
						score = score * 10000000000000
					score = score * 500
				score = score * 2

		if self.boardSpot(state, row-1, col-1) == 'x':
				if self.boardSpot(state, row-2, col-2) == 'x' or self.boardSpot(state, row+1, col+1) == 'x':
					if self.boardSpot(state, row-3, col-3) == 'x' or self.boardSpot(state, row+1, col+1) == 'x':
						score = score * 100000
					score = score * 60
				score = score + 1

		elif self.boardSpot(state, row-1, col-1) == 'o':
				if self.boardSpot(state, row-2, col-2) == 'o' or self.boardSpot(state, row+1, col+1) == 'o':
					if self.boardSpot(state, row-3, col-3) == 'o' or self.boardSpot(state, row+1, col+1) == 'o':
						score = score * 10000000000000
					score = score * 500
				score = score * 2

		if self.boardSpot(state, row-1, col) == 'x':
				if self.boardSpot(state, row-2, col) == 'x' or self.boardSpot(state, row+1, col+1) == 'x':
					if self.boardSpot(state, row-3, col) == 'x' or self.boardSpot(state, row+1, col+1) == 'x':
						score = score * 100000
					score = score * 60
				score = score + 1

		elif self.boardSpot(state, row-1, col) == 'o':
				if self.boardSpot(state, row-2, col) == 'o' or self.boardSpot(state, row+1, col) == 'o':
					if self.boardSpot(state, row-3, col) == 'o' or self.boardSpot(state, row+1, col) == 'o':
						score = score * 10000000000000
					score = score * 500
				score = score * 2

		if self.boardSpot(state, row-1, col+1) == 'x':
				if self.boardSpot(state, row-2, col+2) == 'x' or self.boardSpot(state, row+1, col-1) == 'x':
					if self.boardSpot(state, row-3, col+3) == 'x' or self.boardSpot(state, row+1, col-1) == 'x':
						score = score * 100000
					score = score * 60
				score = score + 1

		elif self.boardSpot(state, row-1, col+1) == 'o':
				if self.boardSpot(state, row-2, col+2) == 'o' or self.boardSpot(state, row+1, col-1) == 'o':
					if self.boardSpot(state, row-3, col+3) == 'o' or self.boardSpot(state, row+1, col-1) == 'o':
						score = score * 10000000000000
					score = score * 500
				score = score * 2

		if self.boardSpot(state, row, col+1) == 'x':
				if self.boardSpot(state, row, col+2) == 'x' or self.boardSpot(state, row, col-1) == 'x':
					if self.boardSpot(state, row, col+3) == 'x' or self.boardSpot(state, row, col-1) == 'x':
						score = score * 100000
					score = score * 60
				score = score + 1

		elif self.boardSpot(state, row, col+1) == 'o':
				if self.boardSpot(state, row, col+2) == 'o' or self.boardSpot(state, row, col-1) == 'o':
					if self.boardSpot(state, row, col+3) == 'o' or self.boardSpot(state, row, col-1) == 'o':
						score = score * 10000000000000
					score = score * 500
				score = score * 2

		if self.boardSpot(state, row+1, col+1) == 'x':
				if self.boardSpot(state, row+2, col+2) == 'x' or self.boardSpot(state, row-1, col-1) == 'x':
					if self.boardSpot(state, row+3, col+3) == 'x' or self.boardSpot(state, row-1, col-1) == 'x':
						score = score * 100000
					score = score * 60
				score = score + 1

		elif self.boardSpot(state, row+1, col+1) == 'o':
				if self.boardSpot(state, row+2, col+2) == 'o' or self.boardSpot(state, row-1, col-1) == 'o':
					if self.boardSpot(state, row+3, col+3) == 'o' or self.boardSpot(state, row-1, col-1) == 'o':
						score = score * 10000000000000
					score = score * 5
				score = score * 2

		return score

	def boardSpot(self, state, row, col):
		if row in range(6):
			if col in range(7):
				return state[row][col]
		else:
			return False;