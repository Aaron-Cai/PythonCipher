__author__ = 'Aaron'

import pyperclip,sys,os

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def translateMessage(key,message,mode):
	translated = []

	keyIndex = 0;
	key = key.upper()

	for symbol in message:
		num = LETTERS.find(symbol.upper())
		if num!= -1:
			if mode == 'encrypt':
				num += LETTERS.find(key[keyIndex])
			elif mode == 'decrypt':
				num -= LETTERS.find(key[keyIndex])
			num %= len(LETTERS)

			if symbol.isupper():
				translated.append(LETTERS[num])
			elif symbol.islower():
				translated.append(LETTERS[num].lower())
			keyIndex += 1
			keyIndex %= len(key)
		else:
			translated.append(symbol)

	return ''.join(translated)

def encryptMessage(key,message):
	return translateMessage(key,message,'encrypt')
def decryptMessage(key,message):
	return translateMessage(key,message,'decrypt')


def main():
	if(len(sys.argv) != 4):
		print 'invalid input'
	else:
		inputFileName = sys.argv[-3]
		outputFileName = sys.argv[-2]
		mode = sys.argv[-1]

		if not os.path.exists(inputFileName):
			print 'file '+ inputFileName + ' does not exit'

	key = 'ASIMOV'

	message = open(inputFileName).read()

	if mode == 'encrypt':
		translated = encryptMessage(key,message)
	elif mode == 'decrypt':
		translated = decryptMessage(key,message)

	print ''
	print ''
	print ''

	print 'Key: ' + key



	print mode + ' result'

	print translated[:200]

	print 'saving as ' + outputFileName + '...'

	open(outputFileName,'w').write(translated)
	print 'done'


if __name__ == '__main__':
	main()



