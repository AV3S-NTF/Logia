from math import*

def replace(word, first):
    length = len(word)

    done = False

    returnWord = ""

    number = str(int(word[first]) + int(word[first + 1]))

    which = len(number)
    
    for i in range(0, length - 1):
        if (done != True):
            if (i == first):
                returnWord += number[which - 1]
                done = True
            else:
                returnWord += word[i]
        else:
            returnWord += word[i + 1]

    return returnWord

def main(number):
    done = False

    count = 0
    
    word = number

    length = len(number)

    while(done != True):
        count = 0
        length = len(word)
        for i in range(0, length - 1):
            if (word[i] == word[i + 1]):
                word = replace(word, i)
                i += 1
                count += 1
        if (count == 0):
            done = True                    

    print(word)

main("84211")
