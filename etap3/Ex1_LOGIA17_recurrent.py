from math import*

def litera(sentence):
    alphabet = [0 for i in range(0, 26)]

    processedSentence = ''.join(sentence)
    
    def recurrent(sentence, biggest, alphabet, result):
        if (len(sentence) <= 0):
            return result
        else:
            index = ord(sentence[0]) - 97
            alphabet[index] += 1;
            if (alphabet[index] > biggest):
                result = [0]
                result[0] = chr(index + 97)
                biggest = alphabet[index]
            elif (alphabet[index] == biggest):
                result.append(chr(index + 97))
            return recurrent(sentence[1:], biggest, alphabet, result)

    result = recurrent(processedSentence, 0, alphabet, [])
    if (len(result) == 1):
        result = result[0]
    
    return result

print(litera(['julka','lubi','psy']))
