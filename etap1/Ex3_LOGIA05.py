from turtle import*
from math import*
from time import*
import random

#speed(0)

random.seed(gmtime())

def main():
    n = 150
    a = 0
    penup()
    rt(90)
    fd(150)
    lt(90)
    pendown()
    for i in range(0, 6):
        a = random.randint(3, 6)
        circle(n)
        circle(n, random.randint(1, 3) * (360 / a))
        n = n * ((a - 1) / a)

main()

