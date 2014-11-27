#import pyperclip
import sys

def caesarCipher(message, mode):
	key = 13;
	LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	translated = ''
	message = message.upper()
	for symbol in message:
		if symbol in LETTERS:
			num = LETTERS.find(symbol)
			if mode == 'encrypt':
				num = num + key
			elif mode == 'decrypt':
				num = num - key
			if(num >= len(LETTERS)):
				num = num - len(LETTERS)
			elif num < 0:
				num = num + len(LETTERS)
			translated = translated + LETTERS[num]
		else:
			translated = translated + symbol
	return translated


def main():
	if len(sys.argv) < 3:
		print 'caesarCipher -message -mode\ne.g. caesarCipher Hello world! encrypt '
	else:
		mode = sys.argv[-1];
		message = sys.argv[1];
		for x in xrange(2,len(sys.argv)-1):
			message  = message +' '+ sys.argv[x]
			
		print 'input: ' + message
		print 'output: ' + caesarCipher(message,mode)

if __name__ == '__main__':
	main()

