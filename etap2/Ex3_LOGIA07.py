from math import*

def wordToNumbers(word):
    number = ""

    length = len(word)

    for i in range(0, length):
        number += str(int(ord(word[i]) - 49) - 48)

    return int(number)

def sumas(word1, word2):
    added = 0

    returnString = ""

    added = wordToNumbers(word1) + wordToNumbers(word2)

    added = str(added)

    length = len(str(added))

    for i in range(0, length):
        returnString += chr(ord(added[i]) + 49)

    return returnString

def testItem(word1, word2, eResult):
    result = sumas(word1, word2)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem("j", "j", "bi")
    testItem("baab", "jjj", "caaa")
    testItem("bji", "caac", "ccaa")

test()
