from turtle import*
from math import*

speed(0)
delay(0)

LENGHT = 10
n = sqrt(2) * LENGHT

def square1():
    fillcolor("lightblue")
    pencolor("lightblue")
    begin_fill()
    for i in range(0, 4):
        fd(LENGHT)
        lt(90)
    end_fill()
    
def square2():
    fillcolor("lightblue")
    pencolor("lightblue")
    begin_fill()
    for i in range(0, 4):
        fd(n)
        lt(90)
    end_fill()
    
def triangle():
    fillcolor("darkgreen")
    pencolor("darkgreen")
    begin_fill()
    fd(2 * LENGHT)
    lt(135)
    fd(n)
    lt(90)
    fd(n)
    lt(135)
    end_fill()

def part():
    for i in range(0, 4):
        square1()
        penup()
        fd(LENGHT)
        pendown()
        triangle()
        penup()
        fd(3 * LENGHT)
        lt(90)
        pendown()
    penup()
    fd(LENGHT)
    lt(45)
    fd(n)
    pendown()
    square2()
    penup()
    rt(90)
    fd(n)
    lt(45)
    bk(3 * LENGHT)
    pendown()

def main():
    for i in range(0, 5):
        for y in range(0, 3):
            part()
            penup()
            lt(90)
            fd(4 * LENGHT)
            rt(90)
            pendown()
        penup()
        rt(90)
        fd(12 * LENGHT)
        lt(90)
        fd(4 * LENGHT)
        pendown()
        
main()
    
