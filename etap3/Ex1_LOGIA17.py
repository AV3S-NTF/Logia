from math import*

def litera(sentence):
    alphabet = [0 for i in range(0, 26)]
    lengthS = len(sentence)
    length = 0
    for y in range(0, lengthS):
        length = len(sentence[y])
        for i in range(0, length):
            index = ord(sentence[y][i]) - 97
            alphabet

litera("mama")
