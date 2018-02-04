from math import*

def kosp(word0, word1):
    fine = 0
    
    path0 = []
    path1 = []

    foundCommon = False
    commonPath = []

    for i in range(0, int(len(word0) / 2)):
        path0.append([word0[2 * i], word0[2 * i + 1]])

    for i in range(0, int(len(word1) / 2)):
        path1.append([word1[2 * i], word1[2 * i + 1]])
        
    for index0, letter0 in enumerate(path0):
        for index1, letter1 in enumerate(path1):
            if (letter0[0] == letter1[0]):
                foundCommon = True
                commonPath.append(index0)
                commonPath.append(index1)

    print(foundCommon, commonPath)

    if (foundCommon):
        for i in range(0, commonPath[0]):
            fine += int(path0[i][1])
        for i in range(0, commonPath[1]):
            fine += int(path1[i][1])
    else:
        for letter in path0:
            fine += int(letter[1])
        for letter in path1:
            fine += int(letter[1])

    return fine

def testItem(path1, path2, eResult):
    result = kosp(path1, path2)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem("D3E5J8", "H3I2E4J", 8)
    testItem("A3T5U6", "B4G1Y4", 23)

test()
