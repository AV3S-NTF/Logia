from math import*

def main(results, n):
    length = int(len(str(results)) / (2 * n))

    a = 0
    o = 0
    ac = 0
    oc = 0

    for i in range(0, length):
        for y in range(0, n):
            a += int(str(results)[y + 2 * n * i])
        for t in range(0, n):
            o += int(str(results)[n + t + 2 * n * i])
        if (a > o):
            ac += 1
        elif (o > a):
            oc += 1
        else:
            ac += 1
            oc += 1
        a = 0
        o = 0
            
    if (oc > ac):
        return "Olek"
    elif (ac > oc):
        return "Alek"
    else:
        return "Remis"

print(main(242152531514235513, 3))
