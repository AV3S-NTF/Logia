from math import*
from turtle import*

speed(0)
delay(0)

def hexagon(color):
    fillcolor(color)
    for i in range(0, 6):
        for y in range(0, 3):
            fd(80)
            lt(120)
        fd(40)
        rt(60)
    begin_fill()
    for i in range(0, 6):
        fd(40)
        rt(60)
    end_fill()

def main(number):
    input = str(number)

    word = ""

    count = 0

    for i in range(0, 10):
        for y in range(0, 9):
            if (int(input[y]) == i):
                count += 1
        word += str(count)
        count = 0

    rt(30)

    for i in range(0, 3):
        if (word[i] == "0"):
            hexagon("red")
        elif (word[i] == "1"):
            hexagon("yellow")
        else:
            hexagon("darkblue")
        fd(120)
        lt(180)
        if (word[i + 1] == "0"):
            hexagon("red")
        elif (word[i + 1] == "1"):
            hexagon("yellow")
        else:
            hexagon("darkblue")
        lt(60)
        fd(80)
        rt(180)
        if (word[i + 2] == "0"):
            hexagon("red")
        elif (word[i + 2] == "1"):
            hexagon("yellow")
        else:
            hexagon("darkblue")
        fd(120)
        rt(120)
        fd(40)
        lt(120)
        fd(40)
        rt(60)
    
main(321458973)
