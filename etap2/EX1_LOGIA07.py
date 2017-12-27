from turtle import*
from math import*

speed(0)
delay(0)

def triangle(n, LENGTH):
    fillcolor("white")
    if (n == 1):
        fillcolor("black")
    begin_fill()
    for i in range(0, 3):
        fd(LENGTH)
        lt(120)
    end_fill()
    fd(LENGTH)
    fillcolor("white")
    if (n == 3):
        fillcolor("black")
    begin_fill()
    for i in range(0, 3):
        fd(LENGTH)
        lt(120)
    end_fill()
    lt(60)
    fillcolor("white")
    if (n == 4):
        fillcolor("black")
    begin_fill()
    for i in range(0, 3):
        fd(LENGTH)
        lt(120)
    end_fill()
    fd(LENGTH)
    lt(60)
    fillcolor("white")
    if (n == 2):
        fillcolor("black")
    begin_fill()
    for i in range(0, 3):
        fd(LENGTH)
        lt(120)
    end_fill()
    lt(60)
    fd(LENGTH)
    lt(60)
    fd(LENGTH)
    lt(120)

def main(n):
    a = n
    times = 0
    t = 0
    c = 0
    t = n / 4
    c = n - (t * 4)
    t = t + (c / 3)
    c = c - (c / 3)
    t = t + (c / 2)
    length = 500 / t
    while(a != 0):
        if (a > 4):
            triangle(4, length)
            times = times + 1
            penup()
            if (times % 2 == 0):
                lt(60)
                fd(2 * LENGTH)
                lt(120)
            else:
                lt(60)
                fd(2 * length)
                rt(60)
                fd(2 * length)
                lt(180)
            pendown()
main(1)
