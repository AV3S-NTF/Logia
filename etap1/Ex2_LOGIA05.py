from turtle import*
from math import*

speed(0)
delay(0)

def hex():
    for i in range(0, 6):
        fd(20)
        lt(60)

def circle(n):
    for i in range(0, 6):
        for y in range(0, n - 1):
            hex()
            fd(20)
            lt(60)
            fd(20)
            rt(60)
        lt(120)
        fd(20)
        rt(60)

def main(n):
    rt(60)
    for i in range(0, n):
        circle(n - i)
        penup()
        lt(120)
        fd(20)
        rt(60)
        fd(20)
        rt(60)
        pendown()

main(100)
    
