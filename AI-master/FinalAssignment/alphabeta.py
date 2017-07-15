# Minimax AI for Connect 4 with alpha-beta pruning
# @author Everett Harding

from minimax import *
import time
class AlphaBeta(Minimax):
    """ alphabeta object that takes a current connect four"""
    timeLimit = 0

    def __init__(self, board):
        #copy the board
        super(AlphaBeta, self).__init__(board)

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
        legal_moves = {}  # will map legal move states to their alpha values
        # for col in range(7):
        #     # if column i is a legal move...
        #     if self.isLegalMove(col, state):
        #         # make the move in column 'col' for curr_player
        #         temp = self.makeMove(state, col, curr_player)
        #         start = time.clock()
        #         legal_moves[col] = self.search(depth-1, temp, opp_player, -1000000, 1000000, curr_player, start, self.timeLimit/7)

        legal_moves , maxDepth= self.iterativeDeep(depth, timeLimit, state, curr_player, opp_player)
        #print("Depth reached: ", maxDepth)
        best_alpha = -99999999
        best_move = None
        moves = legal_moves.items()
        random.shuffle(list(moves))
        for move, alpha in moves:
            # print("Compare", alpha,move, "to", best_alpha,best_move)
            if alpha >= best_alpha:
                best_alpha = alpha
                best_move = move

        return best_move, best_alpha, maxDepth

    # iterative deepening wrapper for alphabeta search
    def iterativeDeep(self, depth, timeLimit, state, curr_player, opp_player):
        d = 0
        startTime = time.clock()
        legal_moves = {}
        alpha = -100000
        beta = 100000
        while d <= depth and time.clock() - startTime <= timeLimit:
            for col in range(7):
                if self.isLegalMove(col, state):
                    # make the move in column 'col' for curr_player
                    temp = self.makeMove(state, col, curr_player)
                    substart = time.clock()
                    legal_moves[col] = self.search(d, temp, opp_player, alpha, beta, curr_player, substart, timeLimit/7)
            d += 1
        return legal_moves, d-1

    # based on pseudocode from wikipedia
    def search(self, depth, state, curr_player, alpha, beta, me, startTime, limit):
        """ minimax search with alpha-beta pruning"""
        children = []

        for col in range (7):
            if self.isLegalMove(col, state):
                temp = self.makeMove(state, col, curr_player)
                children.append(temp)
        children = sorted(children, key = lambda x: -self.value(x, me))
        # determine opponent's color
        if curr_player == self.colors[0]:
            opp_player = self.colors[1]
        else:
            opp_player = self.colors[0]

        if len(children) == 0 or time.clock() - startTime >= limit or depth == 0 :
            #print("Max Depth heuristic : ", self.value(state, curr_player))
            # for row in temp:
            #     print(row)
            # print("\n")
            # print("Value:", self.value(state, me))
            # input("continue?\n")
            return self.value(state, me)
        if self.gameIsOver(state):
            return self.value(state, me)

        if curr_player is me:
            #do max search
            val = -10000000
            for child in children:
                val = max(val, self.search(depth - 1, child, opp_player, alpha, beta, me, startTime, limit))
                alpha = max(alpha, val)
                if(beta <= alpha):
                    return alpha
                if time.clock() - startTime >= limit:
                    return val
            return val
        else :
            #do min search
            val = 10000000
            for child in children:
                val = min(val, self.search(depth - 1, child, opp_player, alpha, beta, me, startTime, limit))
                beta = min(beta, val)
                if (beta <= alpha):
                   return beta
                if time.clock() - startTime >= limit:
                   return val
            return val

    # def value(self, state, color):
    #     """ Simple heuristic to evaluate board configurations
    #         Heuristic is (num of 4-in-a-rows)*99999 + (num of 3-in-a-rows)*100 +
    #         (num of 2-in-a-rows)*10 - (num of opponent 4-in-a-rows)*99999 - (num of opponent
    #         3-in-a-rows)*100 - (num of opponent 2-in-a-rows)*10
    #     """
    #     if color == self.colors[0]:
    #         o_color = self.colors[1]
    #     else:
    #         o_color = self.colors[0]
    #
    #     my_fours = self.checkForStreak(state, color, 4)
    #     my_threes = self.checkForStreak(state, color, 3)
    #     my_twos = self.checkForStreak(state, color, 2)
    #     opp_fours = self.checkForStreak(state, o_color, 4)
    #     opp_threes = self.checkForStreak(state, o_color, 3)
    #     opp_twos = self.checkForStreak(state, o_color, 2)
    #     if opp_fours > 0:
    #         return -10000000
    #     else:
    #         return my_fours * 100000 + my_threes * 100 + my_twos - (opp_threes *150 + opp_twos)
