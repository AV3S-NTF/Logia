from math import*

def checkNextPrime(number):
    count = number + 1

    while(not checkPrime(count)):
        count += 1

    return count

def checkPrime(number):
    length = int(number / 2)

    if (number == 4):
        return False;

    for i in range(2, length):
        if (number % i == 0):
            return False

    return True

def llpp(pocz, kon):
    count = 0

    prime = 0

    for i in range(pocz, kon):
        if (checkPrime(i)):
            if ((prime + i) / 2 < kon and (prime + i) / 2 > pocz):
                count += 1
            prime = i

    if ((prime + checkNextPrime(prime)) / 2 < kon):
        count += 1

    return count

def test():
    testPart(5, 7, 1)
    testPart(7, 16, 3)
    testPart(2, 38, 11)
    testPart(6, 10, 1)
    testPart(18, 39, 4)

def testPart(pocz, kon, eResult):
    result = llpp(pocz, kon)
    if (result == eResult):
        print("OK")
    else:
        print("BUG", result, eResult)

test()
#print(5 + checkNextPrime(5) / 2 < 7)
#print(5, "+", checkNextPrime(5), "/ 2 < 7")
#print(5 + checkNextPrime(5) / 2)
