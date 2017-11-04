from turtle import*
from math import*

speed(0)
delay(0)

def litera(a, b):
    fillcolor("yellow")
    for i in range(0, 5):
        if (a[i] == 'b'):
            fillcolor("blue")
        begin_fill()
        for y in range(0, 4):
            fd(b)
            lt(90)
        end_fill()
        fd(b)
        fillcolor("yellow")
    bk(5 * b)

def find(x):
    return {
        'A': 'aaaaa',
        'B': 'aaaab',
        'C': 'aaaba',
        'D': 'aaabb',
        'E': 'aabaa',
        'F': 'aabab',
        'G': 'aabba',
        'H': 'aabbb',
        'I': 'abaaa',
        'J': 'abaaa',
        'K': 'abaab',
        'L': 'ababa',
        'M': 'ababb',
        'N': 'abbaa',
        'O': 'abbab',
        'P': 'abbba',
        'Q': 'abbbb',
        'R': 'baaaa',
        'S': 'baaab',
        'T': 'baaba',
        'U': 'baabb',
        'V': 'baabb',
        'W': 'babaa',
        'X': 'babab',
        'Y': 'babba',
        'Z': 'babbb',
    }[x]

def main(n):
    a = len(n)
    b = 700 / a
    if(a < 5):
        b = 400 / 5
    lt(90)
    for i in range(0, a):
        litera(find(n[i]), b)
        penup()
        rt(90)
        fd(b)
        lt(90)
        pendown()
    penup()
    lt(90)
    fd((a + 1) * b)
    rt(90)
    pendown()

main('MYHEADHURTSAAAABUFAOSD')
