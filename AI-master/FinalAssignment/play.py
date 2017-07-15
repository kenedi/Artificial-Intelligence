# Python Final Project
# Connect Four
#
# Erik Ackermann
# Charlene Wang
#
# Play connect four
# February 27, 2012
 
# from connect4 import *
from connect4 import *
import time

def main():
    """ Play a game!
    """
    print("Which game variant? Please pick a number:")
    print("1 = MiniMax vs AlphaBeta")
    print("2 = MiniMax vs Greedy")
    print("3 = AlphaBeta vs AlphaBeta")
    variant = int(input("Enter number now: "))
    gameCount = int(input("How many games should they play? "))
    maxTestTime = int(input("How many seconds can they search for? "))
    g = Game(maxTestTime, variant)
    g.printState()
    player1 = g.players[0]
    player2 = g.players[1]
    # maxTestTime = int(input("Test up to how many seconds?"))
    games = 0
    win_counts = [0, 0, 0] # [p1 wins, p2 wins, ties]
    player1Depths = []
    player2Depths = []
    exit = False
    # limit = maxTestTime
    # while limit <= maxTestTime:
    while True:
        p1 = False
        while not g.finished:
            if p1:
                player1Depths.append(g.nextMove())
            else:
                player2Depths.append(g.nextMove())
            p1  =  not p1

        g.findFours()
        g.printState()

        if g.winner == None:
            win_counts[2] += 1

        elif g.winner == player1:
            win_counts[0] += 1

        elif g.winner == player2:
            win_counts[1] += 1
     
        printStats(player1, player2, win_counts)
        
        if games == gameCount-1:
            break
        
        games += 1
        time.sleep(2)
        g.newGame(maxTestTime)
        g.printState()

 
        # x = 0
        # print("Move #\tPlayer1\tPlayer2\t")
        # for num in player1Depths:
        #     print(x, "\t\t", num, "\t\t", player2Depths[x])
        #     x+=1
        # limit +=1
 


def printStats(player1, player2, win_counts):
    print("{0}: {1} wins, {2}: {3} wins, {4} ties".format(player1.name,
        win_counts[0], player2.name, win_counts[1], win_counts[2]))
 
if __name__ == "__main__": # Default "main method" idiom.
    main()