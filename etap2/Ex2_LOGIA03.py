from math import*

def LC(word):
    newWord = ""
    length = int(len(word) / 2)

    for i in range(0, length):
        for y in range(0, int(word[2 * i + 1])):
            newWord += word[2 * i]
    
    return newWord

def testItem(word, eResult):
    result = LC(word)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem("a3n5z1", "aaannnnnz")
    testItem("x7y0a1z2z1c4", "xxxxxxxazzzcccc")

test()
