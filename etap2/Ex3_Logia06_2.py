def szyfr(word, key):

	def charToNumber(char):
		return ord(char) - 97

	def numberToChar(number):
		return chr(number + 97)		

	def toNumber(firstChar, secondChar):
		pairNumber = 26 * charToNumber(firstChar) + charToNumber(secondChar) + key
		if (pairNumber > 675):
			pairNumber -= 676
		return pairNumber

	def fromNumber(number):
		secondChar = numberToChar(number % 26)
		firstChar = numberToChar(int(number / 26))
		return firstChar + secondChar

	def convert(converted, toConvert):
		if (len(toConvert) == 0):
			return converted
		else:
			newConverted = converted + fromNumber(toNumber(toConvert[0], toConvert[1]))
			return convert(newConverted, toConvert[2:])

	return convert("", word)


def testItem(word, key, eResult):
    result = szyfr(word, key)
    if (result == eResult):
        print("OK", result)
    else:
        print("BUG, got ", result, "expected ", eResult)

def test():
    testItem("ab", 1, "ac")
    testItem("abrakadabraa", 500, "thkgdgwguxtg")
	    testItem("dzisiajjestkonkurs", 487, "wsblatccxlmdhgdnkl")

test()    
