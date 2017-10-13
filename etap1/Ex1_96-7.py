from turtle import*
from math import*

speed(0)

TRIANGLE = 300 / sqrt(3)

def motyw():
    for i in range(0, 3):
        fd(TRIANGLE / 2)
        lt(120)
        fd(TRIANGLE / 2)
        bk(TRIANGLE / 2)
        rt(120)
        fd(TRIANGLE / 6)
        lt(120)
        fd(100)
        bk(100)
        rt(120)
        fd(2 * (TRIANGLE / 6))
        lt(150)
        fd(150)
        bk(150)
        rt(30)
    

def rozeta():
    circle(100)
    lt(60)
    motyw()
    rt(30)
    penup()
    fd(100)
    pendown()
    lt(90)
    motyw()

rozeta()
