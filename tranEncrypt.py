import sys
import pyperclip

def transpositionEncrypt(key,message):
	ciphertext = ['']*key
	for col in range(key):
		pointer = col
		while pointer < len(message):
			ciphertext[col] += message[pointer]
			pointer += key

	return ''.join(ciphertext)

def decryptMessage(key, message):
	numOfColumns = int(len(message) / key)+1
	numOfRows = key
	numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

	plaintext = [''] * numOfColumns

	col = 0
	row = 0
	for symbol in message:
		plaintext[col] += symbol

		col += 1
		if(col == numOfColumns) or (col == numOfColumns-1 and row >= numOfRows - numOfShadedBoxes):
			col = 0
			row += 1

	##print plaintext
	return ''.join(plaintext)

def main():
	if(len(sys.argv) < 3):
		print 'input message'
	else:
		mode = sys.argv[-1];
		message =' '.join(sys.argv[1:-1])

		if(mode == 'encrypt'):
			ciphertext =  transpositionEncrypt(8,message)
			print ciphertext
			pyperclip.copy(ciphertext)
		else:
			plaintext = decryptMessage(8,message)
			print plaintext
			pyperclip.copy(plaintext)

	

if __name__ == '__main__':
	main()