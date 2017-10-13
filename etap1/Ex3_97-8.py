from turtle import*
from math import*

speed(0)

def square():
    for i in range(0, 6):
        fd(50)
        lt(90)
    rt(180)

def main(n):
    lt(45)
    for i in range(0, n):
        for y in range(0, n):
            square()
        lt(180)
        for y in range(0, n):
            square()
        penup()
        lt(90)
        square()
        lt(90)
        pendown()

main(5)


raw_input("Press the <ENTER> key to continue...")