from turtle import*
from math import*

speed(0)
delay(0)

def part1(n):
    LENGTH = 150 / n
    rt(90)
    for i in  range(0, n):
        circle(LENGTH / 2)
        penup()
        lt(90)
        fd(LENGTH)
        rt(90)
        pendown()
    penup()
    lt(90)
    bk(150)
    pendown()

def main(n, m):
    DEGREE = 360 / m
    
    for i in range(0, m):
        part1(n)
        lt(DEGREE)

main(5, 3)
