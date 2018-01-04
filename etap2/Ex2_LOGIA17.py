from math import*

def maksos(input):
    biggest = 0

    count = 2

    length = len(input)

    for i in range(0, length - 1):
        if (abs(input[i] - input[i + 1]) <= 3):
            count += 1
            print("+1")
        else:
            count = 1
            print("->1")
        if (count > biggest):
            biggest = count
            print("biggest!")

    return biggest

print(maksos([1, 4, 7, 11, 13, 14, 15, 16, 20]))
