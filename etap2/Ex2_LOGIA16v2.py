from math import*

def checkPass(letter, wasA, wasB):
    if (letter == 'a' and wasA == True):
        return False
    elif (letter == 'b' and wasB == True):
        return False
    elif (letter == 'b' and wasA == False):
        return False
    else:
        return True

def spr(word):

    def checkPass(letter, wasA, wasB):
        if (letter == 'a' and wasA == True):
            return False
        elif (letter == 'b' and wasB == True):
            return False
        elif (letter == 'b' and wasA == False):
            return False
        else:
            return True
        
    
    return 0

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

#test()
print(checkPass('a', False, False))
