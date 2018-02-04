from math import*

def slide(position, shelf, slideDistance):
    returnPosition = position

    for i in range(0, slideDistance):
        if (returnPosition % shelf != 0):
            returnPosition -= 1

    return returnPosition

def kiedy(x, y, z):
    days = 0

    position = 0

    while (position < 1000):
        position += x
        position = slide(position, z, y)
        days += 1
    
    return days

print(kiedy(5, 3, 2))
