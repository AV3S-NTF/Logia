from math import*

def ms(n, housesList):
    neighboursCount = []

    biggest = 0

    notBuilded = True

    for i in range(1, n * n + 1):
        neighboursCount.append(0)
        for y in range(0, len(housesList)):
            if (i == housesList[y]):
                notBuilded = False
        if (notBuilded):
            for y in range(0, len(housesList)):
                if (i == 0):
                    if (i + n == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i + 1 == housesList[y]):
                        neighboursCount[i - 1] += 1
                elif (i == n):
                    if (i + n == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i - 1 == housesList[y]):
                        neighboursCount[i - 1] += 1
                elif (i == n * (n - 1) + 1):
                    if (i + 1 == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i - n == housesList[y]):
                        neighboursCount[i - 1] += 1
                elif (i == n * n):
                    if (i - n == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i - 1 == housesList[y]):
                        neighboursCount[i - 1] += 1
                elif (i % n == 0):
                    if (i - n == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i - 1 == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i + n == housesList[y]):
                        neighboursCount[i - 1] += 1
                elif ((i - 1) % n == 0):
                    if (i - n == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i + 1 == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i + n == housesList[y]):
                        neighboursCount[i - 1] += 1
                elif (i <= n):
                    if (i + n == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i - 1 == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i + 1 == housesList[y]):
                        neighboursCount[i - 1] += 1
                elif (i > n * (n - 1)):
                    if (i - n == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i - 1 == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i + 1 == housesList[y]):
                        neighboursCount[i - 1] += 1
                else:
                    if (i + n == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i - 1 == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i + 1 == housesList[y]):
                        neighboursCount[i - 1] += 1
                    if (i - n == housesList[y]):
                        neighboursCount[i - 1] += 1
        notBuilded = True

    returnList = []

    for i in range(0, n * n):
        if (neighboursCount[i] > biggest):
            del returnList[:]
            returnList.append(i + 1)
            biggest = neighboursCount[i]
        elif (neighboursCount[i] == biggest):
            returnList.append(i + 1)

    print(neighboursCount, returnList)

    return returnList

def testItem(n, housesList, eResult):
    result = ms(n, housesList)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem(4, [9, 10, 14], [13])
    testItem(3, [4, 5, 6], [1, 2, 3, 7, 8, 9])

test()
