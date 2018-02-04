from math import*

def pascal(height, width):
    def getNumber(x, y):
        store = 0
        if (x <= 1 or y <= 1):
            print(1)
            return 1
        else:
            store = getNumber(x - 1, y) + getNumber(x, y - 1)
            print(store)
            return store

    number = getNumber(width, height - width + 1)
    
    return number

print(pascal(10, 7))
