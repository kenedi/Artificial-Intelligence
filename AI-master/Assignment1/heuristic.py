from math import *

#return 0
def heuristic1(node, goal):
    return 0

#return minimum(x, y)
def heuristic2(node, goal):
    y = abs(node.yLocation - goal.yLocation)
    x = abs(node.xLocation - goal.xLocation)
    return min(x,y)

#return maximum(x, y)
def heuristic3(node, goal):
    y = abs(node.yLocation - goal.yLocation)
    x = abs(node.xLocation - goal.xLocation)
    return max(x,y)

#return manhattan distance
def heuristic4(node, goal):
    y = abs(node.yLocation - goal.yLocation)
    x = abs(node.xLocation - goal.xLocation) 
    return (x+y)

#return our admissable heuristic (includes turn values)
def heuristic5(node, goal):
    total = 0
    y = (node.yLocation - goal.yLocation)
    x = (node.xLocation - goal.xLocation)
    manhattan = abs(x) + abs(y)

    if abs(y) != 0 and abs(x) != 0:
        return manhattan+2
    elif x > 0 and node.direction == 0:
        return manhattan
    elif x < 0 and node.direction == 2:
        return manhattan
    elif y > 0 and node.direction == 3:
        return manhattan
    elif y < 0 and node.direction == 1:
        return manhattan
    else:
        return manhattan+1

#return inadmissable heuristic - our heuristic multiplied by 3
def heuristic6(node, goal):
    return heuristic5(node, goal)*3