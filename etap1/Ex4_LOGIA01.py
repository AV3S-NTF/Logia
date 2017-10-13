from turtle import*
from math import*

speed(0)

LENGHT = 5

def part1():
    fd(5 * LENGHT)
    rt(90)
    for i in range(0, 5):
        fd(LENGHT)
        rt(90)
        fd(LENGHT)
        lt(90)
    fd(LENGHT)
    lt(90)
    fd(12 * LENGHT)
    rt(90)
    for i in range(0, 5):
        fd(LENGHT)
        rt(90)
        fd(LENGHT)
        lt(90)
    fd(LENGHT)
    lt(90)
    fd(5 * LENGHT)

def part2():
    part1()
    penup()
    lt(90)
    fd(12 * LENGHT)
    rt(180)
    pendown()
    part1()
    penup()
    bk(12 * LENGHT)
    lt(90)
    pendown()

def main():
    lt(90)
    for i in range(0, 4):
        for y in range(0, 3):
            part2()
            penup()
            fd(13 * LENGHT)
            pendown()
        penup()
        bk(39 * LENGHT)
        rt(90)
        fd(13 * LENGHT)
        lt(90)
        pendown()
    penup()
    lt(90)
    fd(52 * LENGHT)
    rt(180)
    pendown()

main()

raw_input("Press the <ENTER> key to continue...")
