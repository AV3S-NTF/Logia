from math import*

def getNumberFromLocation(x, y):
    pyramid = [[1 for t in range(0, x)] for i in range(0, y)]

    for i in range(1, y):
        for t in range(1, x):
            pyramid[i][t] = pyramid[i][t - 1] + pyramid[i - 1][t]

    return pyramid[y - 1][x - 1]

def pascal(height, width):
    number = 0

    x = width
    y = height - (width - 1)

    number = getNumberFromLocation(x, y)
    
    return number

print(pascal(10, 7))
