from turtle import*
from math import*

speed(0)
delay(0)

def part1(length):
    fillcolor("gold")
    penup()
    fd(2 * length)
    lt(90)
    fd(length)
    lt(90)
    pendown()
    begin_fill()
    for i in range(0, 4):
        fd(2 * length)
        rt(90)
        fd(length)
        rt(90)
        fd(length)
        lt(90)
    end_fill()
    penup()
    lt(90)
    fd(length)
    rt(90)
    fd(2 * length)
    rt(180)
    pendown()

def main(n):
    LENGTH = 400 / ((n * 3) + 1)

    penup()
    bk(200)
    rt(90)
    fd(200)
    lt(90)
    pendown()
    fillcolor("lawngreen")
    begin_fill()
    for i in range(0, 4):
        fd(400)
        lt(90)
    end_fill()
    for i in range(0, n):
        for y in range(0, n):
            part1(LENGTH)
            penup()
            lt(90)
            fd(3 * LENGTH)
            rt(90)
            pendown()
        penup()
        lt(90)
        bk(3 * n * LENGTH)
        rt(90)
        fd(3 * LENGTH)
        pendown()

main(30)
