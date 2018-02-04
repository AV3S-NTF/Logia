from math import*

def ilez(word):
    lonelyLetters = 0
    lonely0 = 0
    lonely1 = 0
    
    length = len(word)

    for i in range(0, length):
        if (word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u" or word[i] == "y"):
            if (lonelyLetters == 0):
                lonelyLetters += 1
                lonely0 = i
            else:
                lonelyLetters += 1
                lonely1 = i

    if (lonelyLetters == 0):
        return -2
    elif (lonelyLetters == 1):
        return -1
    else:
        return lonely1 - (lonely0 + 1)

def testItem(word, eResult):
    result = ilez(word)
    if (result == eResult):
        print("OK")
    else:
        print("BUG", result, eResult)

def test():
    testItem("hokuspokus", 6)
    testItem("klucz", -1)
    testItem("xxx", -2)
    testItem("jestemmaciek", 8)

test()
