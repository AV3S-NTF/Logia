from math import*
from turtle import*
import random

speed(0)
delay(0)

LENGTH = 10

def kolumna(ile):
    randomRange = ile * 25
    column = [0, 0, 0, 0]
    randomNumber = 0
    total = 0
    while(total != ile):
        total = 0
        column = [0, 0, 0, 0]
        for i in range(0, 4):
            randomNumber = random.random() * 100
            if (randomNumber < randomRange):
                column[i] = 1
                total = total + 1
        
    for i in range(0, 4):
        if (column[i] == 1):
            fillcolor("black")
            pencolor("black")
        begin_fill()
        for y in range(0, 4):
            fd(LENGTH)
            lt(90)
        end_fill()
        penup()
        fd(LENGTH)
        pendown()
        fillcolor("white")
        pencolor("white")

def main(n):
    length = len(n)
    penup()
    bk(LENGTH)
    pendown()
        
    for i in range(0, length):
        ile = int(n[i])
        penup()
        fd(LENGTH)
        lt(90)
        pendown()
        kolumna(ile)
        penup()
        bk(4 * LENGTH)
        rt(90)
        pendown()

    penup()
    bk(length * LENGTH)
    pencolor("black")
    pendown()
    
    for i in range(0, 2):
        fd(length * LENGTH)
        lt(90)
        fd(4 * LENGTH)
        lt(90)

main('11223344')
