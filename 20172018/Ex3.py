from math import*

def main(n):
    a = 1 / 3
    ile = 0
    while (n != 0):
        if (a > n):
            n = n - (a / 3)
            a = 1 / 3
            ile = ile + 1
        a = a * 3
    print(ile)

main(29)
