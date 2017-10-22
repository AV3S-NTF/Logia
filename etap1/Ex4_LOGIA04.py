from turtle import*
from math import*

speed(0)

LENGTH = 10

def part1():
    circle(LENGTH, 90)
    circle(-LENGTH, 180)
    circle(LENGTH, 90)

def main(n):
    for y in range(0, 2):
        for i in range(0, n):
            part1()
        circle(-LENGTH, 180)

main(20)
