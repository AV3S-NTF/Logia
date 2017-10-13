from turtle import*
from math import*

speed(0)
delay(0)

LENGHT = 30

def triangle():
    n = sqrt(2) * LENGHT
    pencolor("yellow")
    fillcolor("yellow")
    begin_fill()
    fd(LENGHT)
    lt(135)
    fd(n)
    lt(135)
    fd(LENGHT)
    lt(90)
    end_fill()

def part():
    pencolor("green")
    fillcolor("green")
    begin_fill()
    for i in range(0, 2):
        fd(4 * LENGHT)
        lt(90)
        fd(2 * LENGHT)
        lt(90)
    end_fill()
    for i in range(0, 2):
        triangle()
        penup()
        fd(4 * LENGHT)
        lt(90)
        pendown()
        triangle()
        penup()
        fd(2 * LENGHT)
        lt(90)
        pendown()
    
def main(n, m):
    penup()
    bk(2 * m * LENGHT)
    rt(90)
    fd(n * LENGHT)
    lt(90)
    pendown()
    for i in range(0, m):
        for y in range(0, n):
            part()
            penup()
            lt(90)
            fd(2 * LENGHT)
            rt(90)
            pendown()
        penup()
        rt(90)
        fd(2 * n * LENGHT)
        lt(90)
        fd(4 * LENGHT)
        pendown()

main(10, 10)
