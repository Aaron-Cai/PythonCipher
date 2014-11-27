import sys


def caesarHacker(message):
	LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for key in range(len(LETTERS)):
		translated = ''

		for symbol in message:
			if symbol in LETTERS:
				num = LETTERS.find(symbol)
				num = num - key

				if(num < 0):
					num = num + len(LETTERS)
				translated = translated + LETTERS[num]
			else:
				translated = translated + symbol

		print 'Key#'+ str(key) + ': ' + translated


def  main():
	if len(sys.argv) < 3:
		print 'caesarHacker -encrypt message \ne.g. caesarHacker GUVFKSAFSF'
	else:
		message = sys.argv[1];
		for x in xrange(2,len(sys.argv)):
			message  = message +' '+ sys.argv[x]
			
		print 'crypt: ' + message
		print 'decrypt: '
		caesarHacker(message)
		##print 'output: ' + caesarHacker(message)

if __name__ == '__main__':
	main()