import os,re,copy,pprint,pyperclip,simSubCipher,makeWordPatterns
if not os.path.exists('wordPatterns.py'):
	makeWordPatterns.main()
import wordPatterns


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')


def getBlankCipherLetterMapping():
	return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
			'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P':[],
			 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [],'Y': [], 'Z': []}

def addLettersToMapping(letterMapping,cipherword,candidate):
	letterMapping = copy.deepcopy(letterMapping)
	for i in range(len(cipherword)):
		if candidate[i] not in letterMapping[cipherword[i]]:
			letterMapping[cipherword[i]].append(candidate[i])
	return letterMapping

def intersectMappings(mapA,mapB):
	intersectMapping = getBlankCipherLetterMapping()
	for letter in LETTERS:
		if mapA[letter] == []:
			intersectMapping[letter] = copy.deepcopy(mapB[letter])
		elif mapB[letter] == []:
			intersectMapping[letter] = copy.deepcopy(mapA[letter])
		else:
			for mappedLetter in mapA[letter]:
				if mappedLetter in mapB[letter]:
					intersectMapping[letter].append(mappedLetter)
	return intersectMapping

def removeSolvedLettersFromMapping(letterMapping):
	letterMapping = copy.deepcopy(letterMapping)
	loopAgain = True
	while loopAgain:
		loopAgain = False
		solvedLetters = []
		for cipherLetter in LETTERS:
			if len(letterMapping[cipherLetter]) == 1:
				solvedLetters.append(letterMapping[cipherLetter][0])
		for cipherLetter in LETTERS:
			for s in solvedLetters:
				if len(letterMapping[cipherLetter]) != 1 and s in letterMapping[cipherLetter]:
					letterMapping[cipherLetter].remove(s)
					if len(letterMapping[cipherLetter]) == 1:
						loopAgain = True
	return letterMapping

def hackSimpleSub(message):
	intersectedMap = getBlankCipherLetterMapping()
	cipherwordList = nonLettersOrSpacePattern.sub('',message.upper()).split()
	for cipherword in cipherwordList:
		newMap = getBlankCipherLetterMapping()
		wordPattern = makeWordPatterns.getWordPattern(cipherword)
		if wordPattern not in wordPatterns.allPatterns:
			continue
		for candidate in wordPatterns.allPatterns[wordPattern]:
			newMap = addLettersToMapping(newMap,cipherword,candidate)
		intersectedMap = intersectMappings(intersectedMap,newMap)
	return removeSolvedLettersFromMapping(intersectedMap)

def decryptWithCipherLetterMapping(ciphertext,letterMapping):
	key = ['x'] * len(LETTERS)
	for cipherLetter in LETTERS:
		if len(letterMapping[cipherLetter]) == 1:
			keyIndex = LETTERS.find(letterMapping[cipherLetter][0])
			key[keyIndex] = cipherLetter
		else:
			ciphertext = ciphertext.replace(cipherLetter.lower(),'_')
			ciphertext = ciphertext.replace(cipherLetter.upper(),'_')
	key = ''.join(key)
	return simSubCipher.decryptMessage(key,ciphertext)


def main():
	message1 = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu,\
ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnaji\
sxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia\
esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbm\
lsxao sx jisr elh. -Facjclxo Ctrramm'

	message = 'olqihxirckgnz plqrzkbzb mpbkssiplc'

	print 'Hacking...'

	letterMapping = hackSimpleSub(message1)

	print 'mapping...'
	pprint.pprint(letterMapping)
	print ''
	print 'Original ciphertext:'
	print message1
	print ''
	hackedMessage = decryptWithCipherLetterMapping(message1,letterMapping)
	print 'copying hacked message to clipboard:'
	pyperclip.copy(hackedMessage)
	print hackedMessage


if __name__ == '__main__':
	main()