import pprint

def getWordPattern(word):
	word = word.upper()
	nextNum = 0
	letterNums = {}
	wordPattern = []
	for letter in word:
		if letter not in letterNums:
			letterNums[letter] = str(nextNum)
			nextNum += 1
		wordPattern.append(letterNums[letter])
	return '.'.join(wordPattern)


def main():
	allPatterns = {}

	wordList = open('dict.txt').read().split('\n')

	for word in wordList:
		pattern = getWordPattern(word)
		if pattern not in allPatterns:
			allPatterns[pattern] = [word]
		else:
			allPatterns[pattern].append(word)

	open('wordPatterns.py','w').write('allPatterns =' + pprint.pformat(allPatterns))


if __name__ == '__main__':
	main()