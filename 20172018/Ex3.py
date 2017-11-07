from math import*

def ile(n):
    a = 1 / 3
    il = 0
    while (n != 0):
        if (a > n):
            n = n - (a / 3)
            a = 1 / 3
            il = il + 1
        a = a * 3
    print(il)

ile(64)
