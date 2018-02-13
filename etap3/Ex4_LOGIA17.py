from math import*

def recurrent(record, competitors):
    if (len(competitors) == 1):
        return competitors[0]
    else:
        smallest = record[0][0]
        smallestI = 0
        nCompetitors = []
        for i in range(0, len(record[0])):
            if (record[0][i] < smallest):
                smallest = record[0][i]
                smallestI = i
        for i in range(0, len(record[0])):
            if (i != smallestI):
                nCompetitors.append(competitors[i])
        return recurrent(record[1:], nCompetitors)

def zawody(record):
    length = len(record[0])

    competitors = []

    for i in range(0, length):
        competitors.append(chr(i + 65))

    return recurrent(record, competitors)

def testItem(record, eResult):
    result = zawody(record)
    if (eResult == result):
        print("OK")
    else:
        print("BUG", result, eResult)

def test():
    testItem([[8, 9]], 'B')
    testItem([[4,0,2,1],[1,2,3],[2,1]], 'C')

test()
