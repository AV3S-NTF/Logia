from turtle import*
from math import*

speed(0)
delay(0)

def square(n):
    fillcolor("yellow")
    begin_fill()
    for i in range(0, 4):
        fd(n)
        lt(90)
    end_fill()

def trapez(n):
    m = sqrt(((0.5 * n) * (0.5 * n)) + (n * n))
    fillcolor("purple")
    begin_fill()
    fd(n)
    lt(63.435)
    fd(m)
    lt(116.565)
    fd(2 * n)
    lt(116.565)
    fd(m)
    lt(63.435)
    end_fill()

def part1(n):
    penup()
    fd(2 * n)
    rt(90)
    fd(n / 2)
    lt(180)
    pendown()
    square(n)
    lt(90)
    fd(n)
    rt(90)
    trapez(n)
    penup()
    fd(n / 2)
    lt(90)
    fd(n)
    rt(180)
    pendown()

def part2(n):
    penup()
    fd(3 * n)
    rt(90)
    fd(n / 2)
    lt(90)
    pendown()
    for i in range(0, 4):
        square(n)
        fd(n)
        part1(n)
        bk(n)
        lt(90)
    penup()
    lt(90)
    fd(n / 2)
    lt(90)
    fd(3 * n)
    rt(180)
    pendown()

def main(n):
    m = 600 / (6 * n)
    penup()
    bk(3 * n * m)
    lt(90)
    fd(m / 2)
    rt(90)
    pendown()
    for i in range(0, n):
        part2(m)
        penup()
        fd(6 * m)
        pendown()

main(6)
