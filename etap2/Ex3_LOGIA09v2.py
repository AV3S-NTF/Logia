from math import*

def main(number):
    length = len(number)

    numbers = ""
    
    for i in range(0, length):
        if (number[i] != '1'):
            numbers = numbers + number[i]
    if (len(numbers) > 1):
        print(False)
    elif (numbers[0] == 4 or numbers[0] == 6 or numbers[0] == 8 or numbers[0] == 9):
        print(False)
    else:
        print(True)

main("999")
