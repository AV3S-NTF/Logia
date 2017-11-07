from turtle import*
from math import*

speed(0)
delay(0)

def domek(n):
    m = sqrt(((0.5 * n) * (0.5 * n)) + (n * n))
    fillcolor("lime")
    begin_fill()
    for i in range(0, 4):
        fd(12 * n)
        lt(90)
    end_fill()
    fd(4 * n)
    fillcolor("lightblue")
    begin_fill()
    for i in range(0, 2):
        fd(4 * n)
        lt(90)
        fd(6 * n)
        lt(90)
    end_fill()
    penup()
    lt(90)
    fd(7 * n)
    lt(90)
    fd(3 * n)
    rt(180)
    pendown()
    fillcolor("yellow")
    begin_fill()
    for i in range(0, 4):
        fd(4 * n)
        lt(90)
    end_fill()
    penup()
    fd(6 * n)
    pendown()
    begin_fill()
    for i in range(0, 4):
        fd(4 * n)
        lt(90)
    end_fill()
    penup()
    lt(90)
    fd(5 * n)
    lt(90)
    fd(7 * n)
    rt(180)
    pendown()
    fillcolor("red")
    begin_fill()
    fd(12 * n)
    lt(116.565)
    fd(6 * m)
    lt(63.435)
    fd(6 * n)
    lt(63.435)
    fd(6 * m)
    lt(116.565)
    end_fill()
    penup()
    rt(90)
    fd(12 * n)
    lt(90)
    pendown()

def main(n):
    y = 1.75
    for i in range(0, n):
        y = y * 1.28
    m = 450 / y
    for i in range(0, n):
        domek(int((i * 0.75 * m) / 12))
        penup()
        fd(int(i * 0.75 * m))
        pendown()
    
main(2)
