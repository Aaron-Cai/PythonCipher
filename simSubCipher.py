import sys,random,os,pyperclip


##SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def translateMessage(key,message,mode):
	translated = ''
	charsA = SYMBOLS
	charsB = key
	if mode == 'decrypt':
		charsA,charsB = charsB,charsA
	for symbol in message:

		if symbol.upper() in SYMBOLS:
			if symbol.islower():
		
				translated += charsB[charsA.find(symbol.upper())].lower()
			elif symbol.isupper():
		
				translated += charsB[charsA.find(symbol)].upper()
		else:
	
			translated += symbol
	return translated

def checkValidKey(key):
	keyList = list(key)
	symbolList = list(SYMBOLS)
	keyList.sort()
	symbolList.sort()
	if keyList != symbolList:
		return False;
	else:
		return True

def  getRandomKey():
	key = list(SYMBOLS)
	random.shuffle(key)
	return ''.join(key)

def generateKey():
	key = getRandomKey()
	while not checkValidKey(key):
		key = getRandomKey()
	return key

def encryptMessage(key,message):
	return translateMessage(key,message,'encrypt')

def decryptMessage(key,cipherText):
	return translateMessage(key,cipherText,'decrypt')



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

	key = generateKey()
	##key = """U<Y;Q:5(M=3vP`x/W,u8TV]>$\zj|f0C*X&GE29rdyKp4N7tboSDBc")Lkq!gJ+^1?OR-@{I~Ze._#h[n}FlwHs'mAai%6 """


	if mode == 'encrypt':
		print 'encrypting...'
		translated = encryptMessage(key,message)
	elif mode == 'decrypt':
		print 'decrypting...'
		translated = decryptMessage(key,message)

	print ''
	print ''
	print ''

	print 'Key: ' + str(key)



	print mode + ' result'

	print translated[:200]

	print 'saving as ' + outputFileName + '...'

	open(outputFileName,'w').write(translated)
	print 'done'

	pyperclip.copy(key)





if __name__ == '__main__':
	main()