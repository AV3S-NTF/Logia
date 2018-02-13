from math import*

def checkConditions(order, index):
    if (order[index] == 'n'):
        return 0
    else:
        return 1

def abc(order):
    count = 0

    length = len(order)

    for i in range(0, length):
        count += checkConditions(order, i)
    
    return count

def testItem(order, eResult):
    result = abc(order)
    if (result == eResult):
        print("OK")
    else:
        print("BUG", result, eResult)

def test():
    testItem("nncnnbffbbbccczzzcz", 2)
    testItem("zzzznnnnz", 4)

test()
