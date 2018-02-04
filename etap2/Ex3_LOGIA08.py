from math import*

def maxx(word):
    underword = ""

    starting = 0
    ending = 0

    for index, letter in enumerate(word):
        for i in range(len(word) - 1, index, -1):
            if (i - index > ending - starting and letter == word[i]):
                starting = index
                ending = i

    underword = word[starting:ending + 1]

    if (len(underword) == 0):
        underword = word[0]

    return underword

def testItem(word, eResult):
    result = maxx(word)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem("bbbaaubueytwyetrywax", "aaubueytwyetrywa")
    testItem("abcdefghij", "a")

test()
