from turtle import*
from math import*

speed(0)
delay(0)

LENGHT = 10

def square(n):
    for i in range(0, 4):
        fd(n * LENGHT)
        lt(90)

def pattern():
    square(5)
    lt(90)
    fd(5 * LENGHT)
    rt(180)
    square(4)
    fd(4 * LENGHT)
    lt(90)
    fd(4 * LENGHT)
    lt(90)
    square(3)
    fd(3 * LENGHT)
    lt(90)
    fd(3 * LENGHT)
    lt(90)
    square(2)
    fd(2 * LENGHT)
    lt(90)
    fd(2 * LENGHT)
    lt(90)
    square(1)
    fd(2 * LENGHT)
    rt(90)
    fd(LENGHT)
    lt(90)
    fd(LENGHT)
    rt(90)
    fd(LENGHT)
    lt(90)

def part1():
    fd(5 * LENGHT)
    rt(180)
    pattern()
    fd(LENGHT)
    lt(90)
    fd(12 * LENGHT)
    rt(90)
    fd(6 * LENGHT)
    rt(90)
    fd(5 * LENGHT)
    rt(180)
    pattern()
    bk(5 * LENGHT)
    
def part2():
    part1()
    penup()
    fd(12 * LENGHT)
    lt(180)
    pendown()
    part1()
    penup()
    lt(90)
    fd(12 * LENGHT)
    rt(90)
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
    pensize(2)
    bk(LENGHT)
    for i in range(0, 2):
        fd(40 * LENGHT)
        lt(90)
        fd(53 * LENGHT)
        lt(90)
    lt(90)
    fd(53 * LENGHT)
    penup()
    rt(180)
    fd(LENGHT)
    lt(90)
    fd(LENGHT)
    pendown()

main()

raw_input("Press the <ENTER> key to continue...")
