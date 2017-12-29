from math import*

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def main(number):
    length = len(number)

    potentialPrime = 1

    for i in range(0, length):
        potentialPrime = potentialPrime * (ord(number[i]) - 48)

    print(isprime(potentialPrime))

main("999")
