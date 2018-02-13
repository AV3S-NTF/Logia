from math import*

def calculateDistance(house1, house2, n):
    distance = 0

    distanceX1 = abs(house1[0] - house2[0])
    distanceX2 = abs(house1[0] + (n - house2[0]))
    if (distanceX1 > distanceX2):
        distanceX = distanceX2
    else:
        distanceX = distanceX1

    distanceY1 = abs(house1[1] - house2[1])
    distanceY2 = abs(house1[1] + (n - house2[1]))
    if (distanceY1 > distanceY2):
        distanceY = distanceY2
    else:
        distanceY = distanceY1
    
    return distanceX + distanceY

def planeta(n, houses):
    biggest = 0
    distance = 0

    length = len(houses)

    districts = [[houses[0]]]

    for house in houses:
        for j in range(0, len(districts)):
            for h in range(0, len(districts[j])):
                distance = calculateDistance(house, districts[j][h], n)
                print(distance, house, districts[j][h])
                if (distance <= 5 and districts[j][h] != house):
                    districts[j].append(house)
                    print(j, "Apppended", house)
                else:
                    districts.append([house])
                    
    for i in range(0, len(districts)):
        if (len(districts[i]) > biggest):
            biggest = len(districts[i])
    
    return biggest

def testItem(n, houses, eResult):
    result = planeta(n, houses)
    if (result == eResult):
        print("OK")
    else:
        print("BUG", result, eResult)

def test():
    testItem(12, [[3, 1], [1, 1], [1, 3], [2, 12], [9, 5], [8, 6]], 4)
    testItem(100, [[6, 6], [6, 11], [11, 6], [11, 11], [80, 80]], 4)

test()
