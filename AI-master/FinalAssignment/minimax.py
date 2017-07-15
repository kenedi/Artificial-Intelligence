# Python Final Project
# Connect Four
#
# Erik Ackermann
# Charlene Wang
#
# Connect 4 Module
# February 27, 2012

import random
import time
class Minimax(object):
    """ Minimax object that takes a current connect four board state
    """
    board = None
    colors = ["x", "o"]

    def __init__(self, board):
        # copy the board to self.board
        self.board = [x[:] for x in board]

    def bestMove(self, depth, state, curr_player, timeLimit):
        """ Returns the best move (as a column number) and the associated alpha
            Calls search()
        """

        # determine opponent's color
        if curr_player == self.colors[0]:
            opp_player = self.colors[1]
        else:
            opp_player = self.colors[0]

        # enumerate all legal moves
        # legal_moves = {} # will map legal move states to their alpha values
        # for col in range(7):
        #     # if column i is a legal move...
        #     if self.isLegalMove(col, state):
        #         # make the move in column 'col' for curr_player
        #         temp = self.makeMove(state, col, curr_player)
        #         legal_moves[col] = -self.search(depth-1, temp, opp_player)

        legal_moves, maxDepth = self.iterativeDeep(state, curr_player, depth, timeLimit)
        best_alpha = -99999999
        best_move = 0
        moves = legal_moves.items()
        random.shuffle(list(moves))
        for move, alpha in moves:
            # print("Compare ", alpha, move+1, " to ", best_alpha, best_move+1)
            if alpha >= best_alpha:
                best_alpha = alpha
                best_move = move
        
        return best_move, best_alpha, maxDepth

    def iterativeDeep(self, state, curr_player, depth, timeLimit):
        # determine opponent's color
        if curr_player == self.colors[0]:
            opp_player = self.colors[1]
        else:
            opp_player = self.colors[0]

        d = 0
        startTime = time.clock()
        legal_moves = {}
        while d <= depth and time.clock() - startTime <= timeLimit:
            for col in range(7):
                if self.isLegalMove(col, state):
                    # make the move in column 'col' for curr_player
                    temp = self.makeMove(state, col, curr_player)
                    substart = time.clock()
                    legal_moves[col] = -self.search(d, temp, opp_player, substart, timeLimit / 7)
            d += 1
        return legal_moves, d - 1

    def search(self, depth, state, curr_player, startTime, limit):
        """ Searches the tree at depth 'depth'
            By default, the state is the board, and curr_player is whomever
            called this search

            Returns the alpha value
        """

        # enumerate all legal moves from this state
        legal_moves = []
        for i in range(7):
            # if column i is a legal move...
            if self.isLegalMove(i, state):
                # make the move in column i for curr_player
                temp = self.makeMove(state, i, curr_player)
                legal_moves.append(temp)

        # if this node (state) is a terminal node or depth == 0...
        if depth == 0 or len(legal_moves) == 0  or time.clock() - startTime >= limit:
            # return the heuristic value of node
            return self.value(state, curr_player)
        if self.gameIsOver(state):
            return self.value(state, curr_player)
        # determine opponent's color
        if curr_player == self.colors[0]:
            opp_player = self.colors[1]
        else:
            opp_player = self.colors[0]

        alpha = -99999999
        for child in legal_moves:
            if child is None:
                print("child == None (search)")
            alpha = max(alpha, -self.search(depth-1, child, opp_player, startTime, limit))
            if time.clock() - startTime >= limit:
                return alpha
        return alpha

    def isLegalMove(self, column, state):
        """ Boolean function to check if a move (column) is a legal move
        """

        for i in range(6):
            if state[i][column] == ' ':
                # once we find the first empty, we know it's a legal move
                return True

        # if we get here, the column is full
        return False

    def gameIsOver(self, state):
        if self.checkForStreak(state, self.colors[0], 4) >= 1:
            return True
        elif self.checkForStreak(state, self.colors[1], 4) >= 1:
            return True
        else:
            return False


    def makeMove(self, state, column, color):
        """ Change a state object to reflect a player, denoted by color,
            making a move at column 'column'

            Returns a copy of new state array with the added move
        """

        temp = [x[:] for x in state]
        for i in range(6):
            if temp[i][column] == ' ':
                temp[i][column] = color
                return temp

    def value(self, state, color):
        """ Simple heuristic to evaluate board configurations
            Heuristic is (num of 4-in-a-rows)*99999 + (num of 3-in-a-rows)*100 +
            (num of 2-in-a-rows)*10 - (num of opponent 4-in-a-rows)*99999 - (num of opponent
            3-in-a-rows)*100 - (num of opponent 2-in-a-rows)*10
        """
        if color == self.colors[0]:
            o_color = self.colors[1]
        else:
            o_color = self.colors[0]

        my_fours = self.checkForStreak(state, color, 4)
        my_threes = self.checkForStreak(state, color, 3)
        my_twos = self.checkForStreak(state, color, 2)
        opp_fours = self.checkForStreak(state, o_color, 4)
        opp_threes = self.checkForStreak(state, o_color, 3)
        #opp_twos = self.checkForStreak(state, o_color, 2)
        if opp_fours > 0:
            return -100000
        else:
            return my_fours*10000000 + my_threes*100 + my_twos - opp_threes * 1000

    def checkForStreak(self, state, color, streak):
        count = 0
        # for each piece in the board...
        for i in range(6):
            for j in range(7):
                # ...that is of the color we're looking for...
                if state[i][j].lower() == color.lower():
                    # check if a vertical streak starts at (i, j)
                    count += self.verticalStreak(i, j, state, streak)

                    # check if a horizontal four-in-a-row starts at (i, j)
                    count += self.horizontalStreak(i, j, state, streak)

                    # check if a diagonal (either way) four-in-a-row starts at (i, j)
                    count += self.diagonalCheck(i, j, state, streak)
        # return the sum of streaks of length 'streak'
        return count

    def verticalStreak(self, row, col, state, streak):
        consecutiveCount = 0
        for i in range(row, 6):
            if state[i][col].lower() == state[row][col].lower():
                consecutiveCount += 1
            elif state[i][col] == " ":
                break
            else:
                consecutiveCount = 0
                break

        if consecutiveCount >= streak:
            return 1
        else:
            return 0

    def horizontalStreak(self, row, col, state, streak):
        consecutiveCount = 0
        for j in range(col, 7):
            if state[row][j].lower() == state[row][col].lower():
                consecutiveCount += 1
            elif state[row][j] == " ":
                break
            else:
                consecutiveCount == 0
                break

        if consecutiveCount >= streak:
            return 1
        else:
            return 0

    def diagonalCheck(self, row, col, state, streak):

        total = 0
        # check for diagonals with positive slope
        consecutiveCount = 0
        j = col
        precededBySpace = False
        if j > 0 and row > 0:
            precededBySpace = state[row-1][j-1] == ' '
        for i in range(row, 6):
            if j > 6:
                break
            elif state[i][j].lower() == state[row][col].lower():
                consecutiveCount += 1
            elif state[i][j] == " " or precededBySpace:
                break
            else:
                consecutiveCount = 0
                break
            j += 1 # increment column when row is incremented

        if consecutiveCount >= streak:
            total += 1

        # check for diagonals with negative slope
        consecutiveCount = 0
        j = col
        if j > 0 and row < 5:
            precededBySpace = state[row+1][j-1] == ' '
        for i in range(row, -1, -1):
            if j > 6:
                break
            elif state[i][j].lower() == state[row][col].lower():
                consecutiveCount += 1
            elif state[i][j] == " ":
                break
            else:
                consecutiveCount = 0
                break
            j += 1 # increment column when row is incremented

        if consecutiveCount >= streak:
            total += 1

        return total


