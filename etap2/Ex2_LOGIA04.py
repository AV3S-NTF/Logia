from math import*

x = 'x'
o = 'o'

def checkWin():
    

def checkHorizontalWinX(game):
    
    for i in range(0, 9, 3):
        
    return False

def checkHorizontalWinY(game):
    return False

def checkHorizontalWin(game):
    return 
    
    if (game[0] == x or game[0] == o and game[3] == x or game[3] == o and game[6] == x or game[7] == o):
        return True
    elif (game[0] == x or game[0] == o and game[3] == x or game[3] == o and game[6] == x or game[7] == o):
        return True
    elif (game[0] == x or game[0] == o and game[3] == x or game[3] == o and game[6] == x or game[7] == o):
        return True
    return False

def checkVerticalWin(game):
    if (game[0] == x or game[0] == o and game[1] == x or game[1] == o and game[2] == x or game[2] == o):
        return True
    elif (game[3] == x or game[3] == o and game[4] == x or game[4] == o and game[5] == x or game[5] == o):
        return True
    elif (game[6] == x or game[6] == o and game[7] == x or game[7] == o and game[8] == x or game[8] == o):
        return True
    return False

def checkSlatedWin(game):
    return False

def checkWin(game):
    return False

def kk(game):
    currentX = 0
    currentO = 0

    for letter in game:
        if (letter == x):
            currentX += 1
        elif (letter == o):
            currentO += 1

    #print(x, o)

    if (currentX - currentO >= 2 or currentO - currentX >= 2):
        return False
    
    return True

def testItem(game, eResult):
    result = kk(game)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG", result, eResult)

def test():
    testItem("xwxoxooww", True)
    testItem("xxwowowwo", True)
    testItem("xxoowooww", False)

test()
