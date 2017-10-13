from turtle import*
from math import*

speed(0)

LENGHT = 60

def triangle():
    for i in range(0, 3):
        fd(LENGHT)
        lt(120)

def even(a):
    penup()
    bk((a / 2) * LENGHT)
    rt(90)
    fd((sqrt(0.5 * LENGHT) * a) / 2)
    lt(90)
    pendown()

def Adtriangle(a):
    fd(a * LENGHT)
    lt(120)
    for i in range(0, a):
        triangle()
        fd(LENGHT)
    lt(120)
    fd(a * LENGHT)
    lt(120)
    if(a != 1):
        Adtriangle(a - 1)

def main(a):
    even(a)
    Adtriangle(a)

main(10)
