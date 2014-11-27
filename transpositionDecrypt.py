import sys
import math
import pyperclip


def decryptMessage(key, message):
	numOfColumns = int(len(message) / key)+1
	numOfRows = key
	numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

	plaintext = [''] * numOfColumns

	col = 0
	row = 0
	for symbol in message:
		plaintext[col] += symbol
		print str(col) + "\t " +symbol + "\t " + plaintext[col]

		col += 1
		if(col == numOfColumns) or (col == numOfColumns-1 and row >= numOfRows - numOfShadedBoxes):
			col = 0
			row += 1

	print plaintext
	return ''.join(plaintext)


def main():
	if(len(sys.argv) < 3):
		print 'input message'
	else:
		message =' '.join(sys.argv[1:])
		plaintext = decryptMessage(8, message)

		print plaintext
		pyperclip.copy(plaintext)


if __name__ == '__main__':
	main()