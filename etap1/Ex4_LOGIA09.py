from turtle import*
from math import*

speed(0)
delay(0)

def part1(length):
    trapez = sqrt(2) * length
    fillcolor("limegreen")
    begin_fill()
    fd(length)
    lt(45)
    fd(2 * trapez)
    lt(45)
    fd(length)
    rt(135)
    fd(3 * trapez)
    rt(135)
    fd(3 * length)
    lt(45)
    fd(1.5 * trapez)
    rt(90)
    fd(1.5 * trapez)
    end_fill()
    rt(45)
    begin_fill()
    fd(length)
    rt(45)
    fd(2 * trapez)
    rt(45)
    fd(length)
    lt(135)
    fd(3 * trapez)
    lt(135)
    fd(3 * length)
    rt(45)
    fd(1.5 * trapez)
    lt(90)
    fd(1.5 * trapez)
    end_fill()

def part2(length):
    trapez = sqrt(2) * length
    for i in range(0, 4):
        penup()
        lt(45)
        fd(1.5 * trapez)
        rt(45)
        pendown()
        part1(length)
        penup()
        rt(90)
        fd(1.5 * trapez)
        lt(135)
        pendown()
        lt(90)

def main(n, m):
    lt(90)
    if (n < m):
        LENGTH = 400 / (15 * m)
    else:
        LENGTH = 400 / (15 * n)
    for i in range(0, n):
        for y in range(0, m):
            part2(LENGTH)
            penup()
            fd(15 * LENGTH)
            pendown()
        penup()
        bk(m * 15 * LENGTH)
        rt(90)
        fd(15 * LENGTH)
        lt(90)
        pendown()
    
main(4, 3)
