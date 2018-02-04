from math import*

def powiel(word, number):
    returnWord = ""

    times = str(number)

    length = len(times)

    for index, letter in enumerate(word):
        for i in range(0, int(times[index % length])):
            returnWord += letter

    return returnWord

def testItem(word, number, eResult):
    result = powiel(word, number)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem("krokodyl", 123, "krroookoodddyll")
    testItem("lis", 2005, "ll")

test()
