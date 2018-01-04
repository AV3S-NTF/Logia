from math import*

def checkSame(word):
    first = word[0]

    length = len(word)
    
    for i in range(1, length):
        if (word[i] != first):
            return False

    return True;

def returnList(word, which):
    length = len(word)

    y = 0
    i = 2

    for a in range(0, which):
        y += i
        i += 1

    i -= 1
    
    outcome = ""

    while (y < length):
        outcome += word[y];
        y += i
        i += 1
    
    return outcome

def countColumns(word):
    length = len(word)

    y = 0
    a = 1
    i = 2
    
    while(a <= length):
        y += 1
        a += i
        i += 1

    return y

def kolit(word):
    count = 0

    length = countColumns(word)

    for i in range(0, length):
        if (checkSame(returnList(word, i))):
            count += 1
        
    print(count)
    
kolit('ALAMAKRABY')
