import pyperclip,detectEnglish,tranEncrypt,sys

def hackTransposition(message):
	print 'hacking...'

	for key in range(1,len(message)):
		print str(round(float(key)/len(message),7)*100) + '%'
		decryptedMessage = tranEncrypt.decryptMessage(key,message)

		if(detectEnglish.isEnglish(decryptedMessage)):
			print 'Possible encryption hack,fisrt 500 letters in decrypted message:'
			print 'Key: ' + str(key)
			print decryptedMessage[:500]
			isDone = False
			i = 0
			while(not isDone):
				print 'Enter D for done, Enter C for more message,or just press Enter to continue hacking: '
				i+=1
				response = raw_input('>')
				if(response.lower().startswith('d')):
					return decryptedMessage
				elif(response.lower().startswith('c')):
					print decryptedMessage[500*i:500*i+500]
				else:
					break

	return None


def main():
	if(len(sys.argv) != 3):
		print 'invalid input ' + sys.argv

	inputFileName = sys.argv[-2];
	outputFileName = sys.argv[-1];

	crypptMessage = open(inputFileName).read()

	decryptedMessage =  hackTransposition(crypptMessage)

	if(decryptedMessage != None):
		open(outputFileName,'w').write(decryptedMessage);
	else:
		print 'failed to decrypt'

if __name__ == '__main__':
	main()