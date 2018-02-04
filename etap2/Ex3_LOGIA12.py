from math import*

def deleteChar(word, deleting):
    newWord = ""

    for letter in word:
        if (letter != deleting):
            newWord += letter

    return newWord

def checkDifference(route0, route1):
    length = len(route0)
    if (len(route1) != length):
        return
    count = 0
    for i in range(0, length):
        if (route0[i] != route1[i]):
            count += 1
    if (count > 0):
        count -= 1

    return count

def permutations(path):
    length = len(path)
    if (length == 1):
        return {path}
    else:
        returnList = set()
        for letter in path:
            buffer = deleteChar(path, letter)
            tempList = permutations(buffer)
            for i in tempList:
                returnList.add(letter + i)
        return returnList

def miasta(alicja, tomek, zuzanna):
    result = ""
    smallestError = 100

    tourLength = len(alicja)

    possibilities = sorted(permutations(alicja))
    #print(length)
    currentError = 0

    for path in possibilities:
        currentError = 0
        currentError += checkDifference(path, alicja)
        currentError += checkDifference(path, tomek)
        currentError += checkDifference(path, zuzanna)
        if (smallestError > currentError):
            result = path
            smallestError = currentError
            print(smallestError)

    return result

def testItem(alicja, tomek, zuzanna, eResult):
    result = miasta(alicja, tomek, zuzanna)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem("PLKW", "WPLK", "PWKL", "PWLK")
    testItem("TSG", "TGS", "GST", "TGS")

test()
