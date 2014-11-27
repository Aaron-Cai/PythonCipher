import time, os ,sys,tranEncrypt

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
	fileObj = open(inputFileName)
	content = fileObj.read()
	fileObj.close()

	print mode + 'ing...'

	startTime = time.time()

	if mode == 'encrypt':
		translated = tranEncrypt.transpositionEncrypt(8,content)
	elif mode == 'decrypt':
		translated = tranEncrypt.decryptMessage(8,content)
	totalTime = round(time.time() - startTime, 2);

	print mode + 'time: '+str(totalTime) + ' seconds'

	outputFileObj = open(outputFileName,'w');
	outputFileObj.write(translated)
	outputFileObj.close
			
if __name__ == '__main__':
	main()