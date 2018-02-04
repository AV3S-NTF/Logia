from math import*

def poler(directions):
    startingPointX, startingPointY = 500, 500

    x, y = startingPointX, startingPointY

    length = len(directions)

    maxX = startingPointX
    minX = startingPointX
    maxY = startingPointY
    minY = startingPointY

    for i in range(0, length):
        if (directions[i] == "g"):
            y -= 1
            if (minY > y):
                minY = y
        elif (directions[i] == "d"):
            y += 1
            if (maxY < y):
                maxY = y
        elif (directions[i] == "p"):
            x += 1
            if (maxX < x):
                maxX = x
        elif (directions[i] == "l"):
            x -= 1
            if (minX > x):
                minX = x

    return (maxX - minX) * (maxY - minY)

def testItem(directions, eResult):
    result = poler(directions)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem("ggdp", 2)
    testItem("lllgpdddd", 12)

test()
