from math import*
from turtle import*

speed(0)
delay(0)

def hexagon(size):
    fillcolor("black")
    begin_fill()
    for i in range(0, 6):
        fd(size)
        lt(60)
    end_fill()

def main(number):
    triangleNumber = 1
    
    add = 1

    height = 500

    length = 0

    while(triangleNumber <= number):
        add += 1
        triangleNumber += add

    triangleNumber -= add

    length = (2 * (height / (3 * (add - 2)))) / sqrt(3)

    penup()
    bk((((add - 1) * 3) / 2) * length)
    rt(90)
    fd((((add - 1) * 3) / 2) * length)
    lt(90)
    fd(length)
    pendown()

    for i in range(0, add - 1):
        for y in range(0, add - (i + 1)):
            hexagon(length)
            penup()
            fd(3 * length)
            pendown()
        penup()
        bk(3 * length * (add - (i + 1)))
        lt(60)
        fd(3 * length)
        rt(60)
        pendown()
        
main(15)
