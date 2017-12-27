from turtle import*
from math import*

speed(0)
delay(0)

def encode(colors, key, code):
    encoded = ""
    length = len(colors)
    patternLength = len(code)

    which = 0
    
    for i in range(0, patternLength):
        for y in range(0, length):
            if (colors[y] == code[i]):
                which = y + key
        while (which > length - 1):
            which = which - length
        encoded = encoded + colors[which]
    
    return encoded

def main(colors, key, code):
    length = len(colors) + 1
    pattern = code
    patternLength = len(code)

    if (2 * length > patternLength):
        side = 300 / length
    else:
        side = 600 / patternLength
    
    for i in range(0, length):
        for y in range(0, patternLength):
            if (pattern[y] == 'c'):
                fillcolor("red")
            elif (pattern[y] == 'z'):
                fillcolor("lime")
            elif (pattern[y] == 'x'):
                fillcolor("black")
            elif (pattern[y] == 'b'):
                fillcolor("white")
            elif (pattern[y] == 'f'):
                fillcolor("magenta")
            begin_fill()
            for x in range(0, 4):
                fd(side)
                lt(90)
            end_fill()
            fd(side)
        pattern = encode(colors, key, pattern)
        bk(patternLength * side)
        lt(90)
        fd(side)
        rt(90)

main("bzx", 1, "bzxzb")
