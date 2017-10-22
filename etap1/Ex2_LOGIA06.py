from turtle import*
from math import*

speed(0)
delay(0)

LENGTH = 20

def part1():
    for i in range(0, 6):
        fillcolor("grey")
        begin_fill()
        for y in range(0, 3):
            fd(LENGTH)
            lt(120)
        end_fill()
        fd(LENGTH)
        lt(60)
        fillcolor("black")
        begin_fill()
        for y in range(0, 3):
            fd(LENGTH)
            lt(120)
        end_fill()
        lt(120)
        fd(LENGTH)
        rt(120)

def main(n):
    for i in range(0, n):
        for y in range(0, n - i):
            part1()
            penup()
            fd(2 * LENGTH)
            pendown()
        penup()
        bk((n - i) * 2 * LENGTH)
        lt(60)
        fd(2 * LENGTH)
        rt(60)
        pendown()
    penup()
    lt(60)
    bk(2 * LENGTH)
    rt(60)
    pendown()

main(10)
