import sys

DEFAULT_BLOCK_SIZE = 128

BYTE_SIZE = 256



def getBlocksFromText(message,blockSize = DEFAULT_BLOCK_SIZE):
	print message
	messageBytes = message.encode('ascii')
	print messageBytes
	blockInts = []
	for blockStart in range(0,len(messageBytes),blockSize):
		blockInt = 0;
		for i in range(blockStart,min(blockStart+blockSize,len(messageBytes))):
			blockInt += (messageBytes[i] * (BYTE_SIZE ** (i%blockSize)))
		blockInts.append(blockInt)
	return blockInts

def getTextFromBlocks(blockInts,messageLength,blockSize = DEFAULT_BLOCK_SIZE):
	message = []
	for blockInt in blockInts:
		blockMessage = []
		for i in range(blockSize-1,-1,-1):
			if len(message) + i < messageLength:
				asciiNumber = blockInt // (BYTE_SIZE ** i)
				blockInt = blockInt % (BYTE_SIZE ** i)
				blockMessage.insert(0,chr(asciiNumber))
		message.extend(blockMessage)
	return ''.join(message)

def encryptMessage(message,key,blockSize=DEFAULT_BLOCK_SIZE):
	encryptedBlocks = []
	n,e = key
	for block in getBlocksFromText(message,blockSize):
		encryptedBlocks.append(pow(block,e,n))
	return encryptedBlocks

def decryptMessage(encryptedBlocks,messageLength,key,blockSize = DEFAULT_BLOCK_SIZE):
	decryptedBlocks = []
	n,d = key
	for block in encryptedBlocks:
		decryptedBlocks.append(pow(block,d,n))
	return getTextFromBlocks(decryptedBlocks,messageLength,blockSize)


def readKeyFile(keyFilename):
	content = open(keyFilename).read()
	keySize,n,EorD = content.split(',')
	return (int(keySize),int(n),int(EorD))

def encryptAndWriteToFile(messageFilename,keyFilename,message,blockSize=DEFAULT_BLOCK_SIZE):
	keySize,n,e = readKeyFile(keyFilename)

	if keySize < blockSize * 8:
		sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size. Either increase the block size or use different keys.' % (blockSize * 8, keySize))
	encryptedBlocks = encryptMessage(message,(n,e),blockSize)

	for i in range(len(encryptedBlocks)):
		encryptedBlocks[i] = str(encryptedBlocks[i])
	encryptedContent = ','.join(encryptedBlocks)
	encryptedContent = '%s_%s_%s' % (len(message),blockSize, encryptedContent)

	open(messageFilename,'w').write(encryptedContent)

	return encryptedContent

def readFromFileAndDecrypt(messageFilename,keyFilename):
	keySize,n,d = readKeyFile(keyFilename)
	content = open(messageFilename).read()
	messageLength, blockSize, encryptedMessage = content.split('_')
	messageLength = int(messageLength)
	blockSize = int(blockSize)

	if keySize < blockSize * 8:
		sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size. Either increase the block size or use different keys.' % (blockSize * 8, keySize))
	encryptedBlocks = []
	for block in encryptedMessage.split(','):
		encryptedBlocks.append(int(block))

	return decryptMessage(encryptedBlocks,messageLength,(n,d),blockSize)

def main():
	filename = 'encrypted_file.txt'
	mode = 'encrypt'

	if mode == 'encrypt':
		message = '''"Journalists belong in the gutter because that is where the ruling classes throw their guilty secrets." -Gerald Priestland "The Founding Fathers gave the free press the protection it must have to bare the secrets of government and inform the people." -Hugo Black'''
		pubKeyFilename = 'al_sweigart_pubkey.txt'
		print 'encrypting and writing to ' + filename
		encryptedText = encryptAndWriteToFile(filename,pubKeyFilename,message)
		print 'Encrypted text: '
		print encryptedText
	elif mode == 'decrypt':
		privKeyFilename = 'al_sweigart_pubkey.txt'
		print 'Loading private key from '+ privKeyFilename + ' and decrypting...'

		decryptedText = readFromFileAndDecrypt(filename,privKeyFilename)

		print 'Decrypted text: '
		print decryptedText


if __name__ == '__main__':
	main()
