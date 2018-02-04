from math import*

def checkLonelySound(letter):
    return (letter == 'a' or letter == 'e' or letter == 'y' or letter == 'i' or letter == 'o' or letter == 'u')

def kod(s):
    encoded = ""

    length = len(s)

    wasTogetherSound = False
    wasTogether = 0

    buffer = ''

    encoded += s[0]

    if (not checkLonelySound(s[0])):
        wasTogetherSound = True
    
    for i in range(1, length - 1):
        if (checkLonelySound(s[i])):
            if (wasTogetherSound and wasTogether >= 2):
                encoded += buffer
            encoded += s[i]
            encoded += s[i]
            wasTogetherSound = False
            wasTogether = 0
        elif (not wasTogetherSound):
            wasTogetherSound = True
            wasTogether += 1
            encoded += s[i]
        else:
            wasTogether += 1
        buffer = s[i]

    if (checkLonelySound(s[length - 1]) and not checkLonelySound(s[length - 2])):
        encoded += s[length - 2]
    
    encoded += s[length - 1]
    
    return encoded

def testItem(s, eResult):
    result = kod(s)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem("abrakadabra", "abraakaadaabra")
    testItem("skrzynka", "szyynka")
    testItem("warsztat", "waartaat")

test()
