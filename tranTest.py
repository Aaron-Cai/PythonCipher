import random,sys,tranEncrypt

def main():
	random.seed(42)

	for i in range(100):
		message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4,40)

		message = list(message)
		##print message

		random.shuffle(message)
		##print message

		message = ''.join(message)

		print message[:79]

		for key in range(1,len(message)):
			encrypted = tranEncrypt.transpositionEncrypt(key,message)
			decrypted = tranEncrypt.decryptMessage(key,encrypted)

			if message != decrypted:
				print 'error'
				print decrypted
				sys.exit()
	print 'pass'


if __name__ == '__main__':
	main()