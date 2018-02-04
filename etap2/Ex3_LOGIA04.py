from math import*

def testA(letter):
    return (letter == 'a' or letter == 'e' or letter == 'y' or letter == 'i' or letter == 'o' or letter == 'u')

def szyfr(word, key0, key1):
    buffer = ""
    if (len(word) == 1):
        if (testA(word[0])):
            buffer = ord(word[0]) + key0
        else:
            buffer = ord(word[0]) + key1
        while(buffer > 122):
            buffer -= 26
        return chr(buffer)
    else:
        if (testA(word[0])):
            buffer = ord(word[0]) + key0
        else:
            buffer = ord(word[0]) + key1
        while(buffer > 122):
            buffer -= 26
        return chr(buffer) + szyfr(word[1:], key0, key1)

def testItem(word, key0, key1, eResult):
    result = szyfr(word, key0, key1)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem("abrakadabra", 1, 2, "bdtbmbfbdtb")
    testItem("axeyiz", 2, 4, "cbgakd")

test()
