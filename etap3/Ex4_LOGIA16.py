from math import*

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def nextMovePosition(x, y, direction):
    rx = x
    ry = y
    if (direction == UP):
        ry -= 1
    elif (direction == RIGHT):
        rx += 1
    elif (direction == DOWN):
        ry += 1
    elif (direction == LEFT):
        rx -= 1

    return [rx, ry]

def checkOK(n, x, y, road):
    can = True

    if (x > n or y > n or x < 1 or y < 1):
        can = False
    else:
        for coords in road:
            if (x == coords[0] and y == coords[1]):
                can = False
                break

    return can

def lnp(n, sy, sx):
    count = n * n - 1
    x = sx
    y = sy
    direction = RIGHT
    done = False
    road = [[x, y]]
    
    while (not done):
        move = nextMovePosition(x, y, direction)
        if (not checkOK(n, move[0], move[1], road)):
            direction += 1
            if (direction > LEFT):
                direction = UP
            move = nextMovePosition(x, y, direction)
        if (not checkOK(n, move[0], move[1], road)):
            done = True
        else:
            count -= 1
            
        x = move[0]
        y = move[1]
        road.append([x, y])
    
    return count

def testItem(n, x, y, eResult):
    result = lnp(n, x, y)
    if (result == eResult):
        print("OK")
    else:
        print("BUG", result, eResult)

def test():
    testItem(4, 1, 2, 4)
    testItem(4, 3, 1, 8)
    testItem(4, 4, 4, 15)
    testItem(5, 3, 3, 4)
    testItem(4, 1, 1, 0)

test()
