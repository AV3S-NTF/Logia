from math import*

def maxu(users):
    biggest = 0

    usersT = []

    for i in range(0, len(users)):
        for y in range(users[i][0] - 1, (users[i][0] + users[i][1]) - 1):
            while(y >= len(usersT)):
                usersT.append(0)
            usersT[y] += 1
    print(usersT)

    for number in usersT:
        if (number > biggest):
            biggest = number

    return biggest

def testItem(users, eResult):
    result = maxu(users)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem([[1, 2], [2, 2]], 2)
    testItem([[1, 10], [2, 8], [3, 6]], 3)
    testItem([[1, 2], [2, 3], [1, 10], [2, 2], [5, 5]], 4)

test()
