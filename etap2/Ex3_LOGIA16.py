from math import*

def ms(n, housesList):
    neighboursCoords = set([])

    count = 0

    for i in range(1, n * n):
        for y in range(0, len(housesList)):
            if (i + n == housesList[y] or i - n == housesList[y] or i + 1 == housesList[y] or i - 1 == housesList[y]):
                count += 1
                print("count + 1")
        if (i == 1 or i == n or i == n * (n - 1) + 1 or i == n * n):
            print(i, "needs 2")
            if (count == 2):
                neighboursCoords.add(i)
                print("Added", i)
        elif (i - 1 % n == 0 or i % n == 0 or i > n * (n - 1) or i < n):
            print(i, "needs 3")
            if (count == 3):
                neighboursCoords.add(i)
                print("Added", i)
        else:
            print(i, "needs 4")
            if (count == 4):
                neighboursCoords.add(i)
                print("Added", i)

        count = 0

    print(neighboursCoords)

    return sorted(neighboursCoords)

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
testing = {1, 2}
print(testing)
print(sorted(testing))
print(sorted(testing) == testing)
