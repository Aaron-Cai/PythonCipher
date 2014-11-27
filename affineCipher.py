import sys,pyperclip,random,os


SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def gcd(a,b):
	while a != 0:
		a,b = b%a,a
	return b

def findModInverse(a,m):
	if gcd(a,m) != 1:
		return None
	u1,u2,u3 = 1,0,a
	v1,v2,v3 = 0,1,m
	while v3 != 0:
		q = u3 // v3
		v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
	return u1 % m

def getKeyParts(key):
	keyA = key // len(SYMBOLS)
	keyB = key % len(SYMBOLS)

	return (keyA,keyB)

def checkKeys(keyA,keyB,mode):
	if (keyA == 1 and mode == 'encrypt') or (keyB == 0 and mode == 'encrypt'):
		sys.exit('too weak key,choose a different key')
	if(keyA<0 or keyB<0 or keyB>(len(SYMBOLS)-1)) or (gcd(keyA,len(SYMBOLS)) != 1):
		print 'keyA ' + str(keyA) + ' keyB ' + str(keyB) + ' ' + str(len(SYMBOLS))
		sys.exit('invalid key input')


def encrytMessage(key,message):
	keyA,keyB = getKeyParts(key)
	checkKeys(keyA,keyB,'encrypt')
	ciphertext = ''
	print 'encrypting...'
	for symbol in message:
		if symbol in SYMBOLS:
			symIndex = SYMBOLS.find(symbol)
			ciphertext += SYMBOLS[(symIndex * keyA + keyB)%len(SYMBOLS)]
		else:
			ciphertext += symbol

	return ciphertext


def decryptMessage(key,message):
	keyA,keyB = getKeyParts(key)
	checkKeys(keyA,keyB,'decrypt')
	plainText = ''
	modInverseOfKeyA = findModInverse(keyA,len(SYMBOLS))

	##print 'decrypting...'
	for symbol in message:
		if symbol in SYMBOLS:
			symIndex = SYMBOLS.find(symbol)
			plainText += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
		else:
			plainText += symbol
	return plainText

def getRandomKey():
	while True:
		keyA = random.randInt(2,len(SYMBOLS))
		keyB = random.randInt(2,len(SYMBOLS))
		if(gcd(keyA,len(SYMBOLS)) == 1):
			return keyA * len(SYMBOLS) + keyB



def main():
	if(len(sys.argv) != 4):
		print 'invalid input'
	else:
		inputFileName = sys.argv[-3]
		outputFileName = sys.argv[-2]
		mode = sys.argv[-1]

		if not os.path.exists(inputFileName):
			print 'file '+ inputFileName + ' does not exit'

		if os.path.exists(outputFileName):
			print 'This will overwrite the file ' + outputFileName + '(C)continue or (Q)quit'
			response = raw_input('>')
			if not response.lower().startswith('c'):
				sys.exit()

	message = open(inputFileName).read()

	key = 2023

	if mode == 'encrypt':
		outText = encrytMessage(key,message)
	elif mode == 'decrypt':
		outText = decryptMessage(key,message)

	print ''
	print ''
	print ''

	print 'Key: ' + str(key)

	print mode + 'result'

	print outText[:200]

	print 'saving as ' + outputFileName + '...'

	open(outputFileName,'w').write(outText)

	print 'done'


if __name__ == '__main__':
	main()