import sys

def readBoard(fileName):
    f = open(fileName, "r")
    board = []
    count = 0

    while True:
        line = f.readline()
        if not line: break
        squares = line.split("\t")
        board.append(list())
        for value in squares:
            if len(value) is not 1:
                value = value[:1]
            if value is "S" or value is "G" or value is "#":
                board[count].append(value)
            # elif value[0] is "#":
            #     board[count].append("#")
            elif value != "" and value != "\n":
                board[count].append(int(str.rstrip(value)))
        count += 1
    # TESTING
    # for row in board:
    #     for square in row:
    #         print(square, " ", end='')
    #     print("\n")
    # print("\n")

    return board