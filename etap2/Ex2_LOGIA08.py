from math import*

def checkPerfect(number):
    length = number

    count = 1

    for i in range(2, length - 1):
        if (number % i == 0):
            count += i

    if (number % count == 0):
        return True
    else:
        return False

def ilepd(min, max):
    count = 0

    for i in range(min, max):
        if (checkPerfect(i)):
            count += 1
    
    return count

def testItem(min, max, eResult):
    result = ilepd(min, max)
    if (result == eResult):
        print("OK")
    else:
        print("BUG", result, eResult)

def test():
    testItem(10, 100, 22)
    testItem(10, 20, 4)

test()
