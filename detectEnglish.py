

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDict():
	dictFile = open('dict.txt')
	englishWords = {}
	for word in dictFile.read().split('\n'):
		englishWords[word] = None
	dictFile.close()
	return englishWords

ENGLISH_WORDS = loadDict()

def removeNonLetters(message):
	lettersOnly = []
	for symbol in message:
		if symbol in LETTERS_AND_SPACE:
			lettersOnly.append(symbol)
	return ''.join(lettersOnly)

def getEnglishCount(message):
	message = message.upper()
	message = removeNonLetters(message)
	possibleWords = message.split()
	if possibleWords == []:
		return 0.0

	mathes = 0
	for word in possibleWords:
		if word in ENGLISH_WORDS:
			mathes += 1
	return float(mathes) / len(possibleWords)


def isEnglish(message,wordPercent=20,letterPercent=85):
	return getEnglishCount(message)*100 > wordPercent and float(len(removeNonLetters(message))) / len(message) *100 > letterPercent


