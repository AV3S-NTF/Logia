from turtle import*
from math import*

speed(0)
delay(0)

def rysunek(a, LENGTH):
    TRAPEZ = sqrt(2) * LENGTH
    if (a == 9):
        penup()
        fd(0.5 * LENGTH)
        pendown()
        for i in range(0, 2):
            fd(LENGTH)
            lt(90)
            fd(2 * LENGTH)
            lt(90)
        penup()
        bk(0.5 * LENGTH)
        pendown()
    else:
        lt(45)
        fd(2 * TRAPEZ)
        penup()
        lt(135)
        fd(2 * LENGTH)
        lt(135)
        pendown()
        fd(2 * TRAPEZ)
        penup()
        rt(135)
        fd(2 * LENGTH)
        lt(180)
        pendown()
        if (a < 1):
            return 0
        lt(90)
        fd(2 * LENGTH)
        bk(2 * LENGTH)
        rt(90)
        if (a < 2):
            return 0
        penup()
        fd(2 * LENGTH)
        lt(90)
        pendown()
        fd(2 * LENGTH)
        bk(2 * LENGTH)
        lt(90)
        penup()
        fd(2 * LENGTH)
        rt(180)
        pendown()
        if (a < 3):
            return 0
        penup()
        fd(LENGTH)
        lt(90)
        pendown()
        fd(2 * LENGTH)
        bk(2 * LENGTH)
        lt(90)
        penup()
        fd(LENGTH)
        rt(180)
        pendown()
        if (a < 4):
            return 0
        fd(2 * LENGTH)
        bk(2 * LENGTH)
        if (a < 5):
            return 0
        lt(90)
        fd(2 * LENGTH)
        rt(90)
        fd(2 * LENGTH)
        bk(2 * LENGTH)
        rt(90)
        fd(2 * LENGTH)
        lt(90)
        if (a < 6):
            return 0
        lt(90)
        fd(LENGTH)
        rt(90)
        fd(2 * LENGTH)
        bk(2 * LENGTH)
        rt(90)
        fd(LENGTH)
        lt(90)
        if (a < 7):
            return 0
        fd(0.5 * LENGTH)
        lt(90)
        fd(2 * LENGTH)
        bk(2 * LENGTH)
        lt(90)
        fd(0.5 * LENGTH)
        rt(180)
        if (a < 8):
            return 0
        fd(1.5 * LENGTH)
        lt(90)
        fd(2 * LENGTH)
        bk(2 * LENGTH)
        lt(90)
        fd(1.5 * LENGTH)
        rt(180)
        
def main(n):
    a = len(n)
    length = 720 / ((a * 3) - 1)
    penup()
    bk(360)
    pendown()
    for i in range(0, a):
        rysunek(int(n[i]), length)
        penup()
        fd(3 * length)
        pendown()
    penup()
    bk(360)
    pendown()

main('4543290178583')
