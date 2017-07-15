# Node class
# NORTH = -x direction

from queue import PriorityQueue
from ReadBoard import *
import math
from heuristic import *
from copy import deepcopy

board = readBoard(sys.argv[1])
heuristic = int(sys.argv[2])



NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

openSet = PriorityQueue()
closedSet = []


class Node:

    def __init__(self, xLoc, yLoc, parent, value, movelist):
        self.xLocation = xLoc
        self.yLocation = yLoc
        self.parent = parent
        self.direction = NORTH
        self.cost_to = 0
        self.heuristic = 0
        self.value = value
        self.moveList = deepcopy(movelist)

    def __eq__(self, other):
        if isinstance(other, Node) and other.xLocation == self.xLocation and other.yLocation == self.yLocation:
            return True
        else:
            return False

    def __lt__(self, other):
        selfPriority = self.cost_to + self.heuristic
        otherPriority = other.cost_to + other.heuristic
        return selfPriority < otherPriority

    def __str__(self):
        return str(self.xLocation) + ", " + str(self.yLocation) + ", " + str(self.cost_to) + ", " + str(self.heuristic)


def turnCost(node, toNode):
    xDif = node.xLocation - toNode.xLocation
    yDif = node.yLocation - toNode.yLocation
    nDir = node.direction

    # check is north, go north
    # check is north, go south
    # check is north, go sideways
    if yDif is 0:
        if (nDir == NORTH and xDif > 0) or (nDir == SOUTH and xDif < 0):
            return 0
        elif (nDir == EAST and xDif < 0) or (nDir == WEST and xDif > 0):
            toNode.moveList.append("Turn Right")
            return math.ceil((1 / 3) * node.value)
        elif (nDir == EAST and xDif > 0) or (nDir == WEST and xDif < 0):
            toNode.moveList.append("Turn Left")
            return math.ceil((1/3) * node.value)
        else:
            toNode.moveList.append("Turn Right")
            toNode.moveList.append("Turn Right")
            return math.ceil((2/3) * node.value)
    else:
        if (nDir == WEST and yDif > 0) or (nDir == EAST and yDif < 0):
            return 0
        elif (nDir == NORTH and yDif < 0) or (nDir == SOUTH and yDif > 0):
            toNode.moveList.append("Turn Right")
            return math.ceil((1 / 3) * node.value)
        elif (nDir == NORTH and yDif > 0) or (nDir == SOUTH and yDif < 0):
            toNode.moveList.append("Turn Left")
            return math.ceil((1/3) * node.value)
        else:
            toNode.moveList.append("Turn Right")
            toNode.moveList.append("Turn Right")
            return math.ceil((2/3) * node.value)


def moveCost(node, num):
    if abs(num) > 1:
        node.moveList.append("Jump")
        return 20
    else:
        node.moveList.append("Forward")
        return node.value

