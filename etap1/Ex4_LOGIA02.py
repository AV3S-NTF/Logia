from turtle import*
from math import*

speed(0)
delay(0)

LENGTH = 10

def hex():
    penup()
    lt(30)
    fd(LENGTH)
    lt(120)
    pendown()
    for i in range(0, 6):
        fd(LENGTH)
        lt(60)
    penup()
    lt(60)
    fd(LENGTH)
    rt(210)
    pendown()

def main(n):
    for i in range(0, n):
        for y in range(0, n - i):
            hex()
            penup()
            lt(30)
            fd(LENGTH)
            rt(60)
            fd(LENGTH)
            lt(30)
            pendown()
        penup()
        lt(180)
        for y in range(0, n - i):
            rt(30)
            fd(LENGTH)
            lt(60)
            fd(LENGTH)
            rt(30)
        rt(90)
        fd(LENGTH)
        rt(60)
        fd(LENGTH)
        rt(30)
        pendown()

main(10)
