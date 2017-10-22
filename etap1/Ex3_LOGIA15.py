from turtle import*
from math import*

speed(0)
delay(0)

LENGTH = 10

def part1():
    fillcolor("lightpink")
    for i in range(0, 4):
        for y in range(0, 2):
            begin_fill()
            fd(LENGTH)
            rt(90)
            fd(5 * LENGTH)
            rt(90)
            end_fill()
        fd(LENGTH)
    bk(4 * LENGTH)
    
def part2():
    penup()
    fd(4 * LENGTH)
    lt(90)
    fd(4 * LENGTH)
    rt(90)
    pendown()
    fillcolor("yellow")
    begin_fill()
    for i in range(0, 4):
        fd(LENGTH)
        lt(90)
    end_fill()
    for i in range(0, 4):
        fd(LENGTH)
        rt(90)
        part1()
        lt(180)
    penup()
    bk(4 * LENGTH)
    lt(90)
    bk(4 * LENGTH)
    rt(90)
    pendown()

def main(n, m):
    for i in range(0, n):
        for y in range(0, m):
            part2()
            lt(90)
            fd(9 * LENGTH)
            rt(90)
        lt(90)
        bk(m * 9 * LENGTH)
        rt(90)
        fd(9 * LENGTH)

main(5, 2)
