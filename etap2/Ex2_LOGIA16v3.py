from math import*

def spr(word):
    count = 0
    biggest = 0

    y = 0
    length = len(word)

    newWord = ""

    lengthsList = [0]

    for i in range(0, length):
        if (word[i] == 'a' or word[i] == 'b'):
            newWord += word[i]
            y += 1
            lengthsList.append(0)
            lengthsList[y] += 1
        else:
            lengthsList[y] += 1

    length = len(newWord)

    for i in range(0, length - 1):
        if (newWord[i] == 'a' and newWord[i + 1] == 'b'):
            count += lengthsList[i + 1] + lengthsList[i + 2]
            if (i == 0):
                count += lengthsList[i]
        else:
            count = 0
        if (count > biggest):
            biggest = count
    
    return biggest

def testItem(word, eResult):
    result = spr(word)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem("balon", 0)
    testItem("abrakadabra", 3)
    testItem("arbuz", 5)
    testItem("testab", 6)

test()
