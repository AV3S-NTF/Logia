from math import*

def letterCheck(letter, wasA):
    if (letter == 'a' and wasA == True):
        return True
    elif (letter == 'b' and wasA != True):
        return True
    return False

def spr(word):
    count = 0

    biggest = 0

    length = len(word)

    mLetterLocation = 0

    i = 0

    wasA = False
    wasB = False

    while(i < length):
        if (word[i] == 'a' or word[i] == 'b'):
            mLetterLocation = i
            print("new checkpoint:", i)
        if (not letterCheck(word[i], wasA)):
            count += 1
            print(word[i], "on position", i, "has passed!")
        else:
            i = mLetterLocation
            count = 0
            wasA = False
            wasB = False
            print("A and B set to false.")
            print(word[i], "on position", i, "HASN'T passed!")
            print("Count to 0 and i to", i)
        if (word[i] == 'a'):
            wasA = True
            print("there was A here:", i)
        elif (word[i] == 'b'):
            wasB = True
            print("there was B here:", i)
        if (count > biggest and wasB == True and wasA == True):
            biggest = count
            print("Biggest word increased to", biggest)
        i += 1
        print("+1")

    return count

def testItem(word, eResult):
    result = spr(word)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem("balon", 0)
    testItem("abrakadabra", 3)

test()
