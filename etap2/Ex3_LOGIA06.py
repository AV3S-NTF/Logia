from math import*

def numberToSyllabe(number, key):
    letter0 = number - key
    letter1 = 0

    while(letter0 < 0):
        letter += 676
    
    while(letter0 % 26 != 0):
        letter0 -= 1
        letter1 += 1
    
    letter0 = letter0 / 26
    
    return chr(int(letter0) + 97) + chr(letter1 + 97)

def syllabeToNumber(letter1, letter2, key):
    result = (26 * (ord(letter1) - 97) + (ord(letter2) - 97)) + key

    while(result > 675):
        result -= 676
    
    return result

def szyfr(word, key):
    length = int(len(word) / 2)

    result = ""

    for i in range(0, length):
        result += numberToSyllabe(syllabeToNumber(word[2 * i], word[2 * i + 1], key), 0)

    return result

def testItem(word, key, eResult):
    result = szyfr(word, key)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem("ab", 1, "ac")
    testItem("abrakadabraa", 500, "thkgdgwguxtg")
    testItem("dzisiajjestkonkurs", 487, "wsblatccxlmdhgdnkl")

test()
#print(numberToSyllabe(syllabeToNumber('a', 'a', 2), 0))
