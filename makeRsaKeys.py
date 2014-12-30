import random, sys, os, rabinMiller, cryptomath


def generateKey(keySize):
	print 'generating p prime...'
	p = rabinMiller.generateLargePrime(keySize)
	print 'generating q prime...'
	q = rabinMiller.generateLargePrime(keySize)
	n = p * q

	print 'generating e that is relatively to (p-1)*(q-1)'
	while True:
		e = random.randrange(2 ** (keySize-1),2 ** keySize)
		if cryptomath.gcd(e,(p-1) * (q-1) == 1):
			print 'calcuting d that is mod inverse of e...'
			d = cryptomath.findModInverse(e,(p-1) * (q-1))
			if d != None:
				break
	
	publicKey = (n,e)
	privateKey = (n,d)

	print 'public key'
	print publicKey
	print 'private key'
	print privateKey

	return (publicKey,privateKey)

def makeKeyFiles(name,keySize):
	publicKey,privateKey = generateKey(keySize)

	print 'The public key is a '+str(len(str(publicKey[0]))) + ' digit number and a ' + str(len(str(publicKey[1]))) + ' digit number. '
	print 'Writing public key to file '+name + '_pubkey.txt...'
	open('%s_pubkey.txt'%(name),'w').write('%s,%s,%s'%(keySize,publicKey[0],publicKey[1]))
	print 'The private key is a '+str(len(str(privateKey[0]))) + ' digit number and a ' + str(len(str(publicKey[1]))) + ' digit number. '
	open('%s_privkey.txt'%(name),'w').write('%s,%s,%s'%(keySize,privateKey[0],privateKey[1]))

def main():
	print 'making key files...'
	makeKeyFiles('al_sweigart',1024)
	print 'Key files make.'


if __name__ == '__main__':
	main()