from math import*

def deleteChar(word, deleting):
    newWord = ""

    for letter in word:
        if (letter != deleting):
            newWord += letter

    return newWord

def perm(path):
    length = len(path)
    if (length == 1):
        return {path}
    else:
        returnList = set()
        for letter in path:
            buffer = deleteChar(path, letter)
            tempList = perm(buffer)
            for i in tempList:
                returnList.add(letter + i)
        return returnList

print(sorted(perm("ABCDEF")))      

