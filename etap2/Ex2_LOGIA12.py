from math import*

def decimalToAnother(number, base):
    convertedString = ""
    modString = ""
    
    currentNumber = number
    
    if not number:
        return '0'
    while (currentNumber):
        mod = currentNumber % base
        currentNumber = currentNumber // base
        convertedString = chr(48 + mod + 7 * (mod > 10)) + convertedString
    return convertedString

def IleCyfr(liczba, podstawa):
    return len(decimalToAnother(liczba, podstawa))

def test():
    result = IleCyfr(123456, 10)
    
    if (result == 6):
        print("OK")
    else:
        print("BUG")
        
    result = IleCyfr(1, 5)
    
    if (result == 1):
        print("OK")
    else:
        print("BUG")
        
    result = IleCyfr(255, 2)
    
    if (result == 8):
        print("OK")
    else:
        print("BUG")

    result = IleCyfr(255, 16)
    
    if (result == 2):
        print("OK")
    else:
        print("BUG")
        
test()
