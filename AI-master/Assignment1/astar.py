from Node_Class import *
from heuristic import *
from ReadBoard import *
import time




rows = len(board)
cols = len(board[0])

dummy = Node(-1, -1, None, 99999, [])

for x in range(0, rows):
    for y in range(0, cols):
        if board[x][y] == 'S':
            start_node = Node(x, y, None, 0, ["Start"])
            start_node.cost_to = 1
            board[x][y] = 1
        elif board[x][y] == 'G':
            goal_node = Node(x, y, None, 1, [])
            board[x][y] = 1

current_node = start_node
closedSet.append(start_node)
cycles = 0

def getNeighbors(node):
    xLoc = node.xLocation
    yLoc = node.yLocation

    maxRows = len(board)
    maxCols = len(board[0])

    checkNums = [-1, 1, -3, 3]
    neighbors = []
    for num in checkNums:
        if xLoc + num in range(0, maxRows) and not board[xLoc+num][yLoc] == '#':
            neighbor = Node(xLoc+num, yLoc, node, board[xLoc+num][yLoc], node.moveList)
            if num < 0:
                neighbor.direction = NORTH

            else:
                neighbor.direction = SOUTH
            setHeuristic(neighbor, heuristic)
            neighbor.cost_to = node.cost_to + turnCost(node, neighbor) + moveCost(neighbor, num)
            neighbors.append(neighbor)
            # openSet.put(((neighbor.cost_to + neighbor.heuristic), neighbor))

        if yLoc + num in range(0, maxCols) and not board[xLoc][yLoc+num] == '#':
            neighbor = Node(xLoc, yLoc+num, node, board[xLoc][yLoc+num], node.moveList)
            if num < 0:
                neighbor.direction = WEST
            else:
                neighbor.direction = EAST
            setHeuristic(neighbor, heuristic)
            neighbor.cost_to = node.cost_to + turnCost(node, neighbor) + moveCost(neighbor, num)
            neighbors.append(neighbor)
            #
    return neighbors

def findLowNode():
    lowest = openSet.get()[1]
    closedSet.append(lowest)
    return lowest

def setHeuristic(node, heuristic):
    if heuristic == 1:
        node.heuristic = heuristic1(node, goal_node)
    elif heuristic == 2:
        node.heuristic = heuristic2(node, goal_node)
    elif heuristic == 3:
        node.heuristic = heuristic3(node, goal_node)
    elif heuristic == 4:
        node.heuristic = heuristic4(node, goal_node)
    elif heuristic == 5:
        node.heuristic = heuristic5(node, goal_node)
    elif heuristic == 6:
        node.heuristic = heuristic6(node, goal_node)

def printNodeTrace(node, list):
    if(node.parent is None):
        return [node.value]
    else:
       return printNodeTrace(node.parent, list) + [node.value]

startTime = time.clock()
while not current_node.__eq__(goal_node) and cycles < 10000:


    neighbors = getNeighbors(current_node)
    for node in neighbors:
        #print("neighbor node: ", node)
        if node in closedSet:
            pass
        else:
            openSet.put(((node.cost_to + node.heuristic), node))
            cycles += 1
    #print(openSet)
    current_node = findLowNode()

endTime = time.clock()

print("Time elapsed: ", str(endTime-startTime))
print("Score: ", 500-current_node.cost_to)
print("Number of moves made: ",len(current_node.moveList))    
print("Nodes expanded:", len(closedSet))
print("Branching factor: ", float(len(closedSet))**(1/len(current_node.moveList)))
print("Action Progression:")
for x in range(0, len(current_node.moveList)):
    print(current_node.moveList[x])
print("\n")
