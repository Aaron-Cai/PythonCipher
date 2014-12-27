__author__ = 'Aaron'

import detectEnglish, vigenereCipher, pyperclip

def hackvigenere(ciphertext):
	words = open('dict.txt').readlines()
	for word in words:
		word = word.strip()
		decrytedtext = vigenereCipher.decryptMessage(word,ciphertext)
		if detectEnglish.isEnglish(decrytedtext,40):
			print 'Possible encryption break:'
			print 'key ' + word + ':' + decrytedtext[:100]
			print 'enter d for done ,or just press enter to continue'
			response = raw_input('>')
			if response.upper().startswith('D'):
				return decrytedtext

def main():
	ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
	hackedMessage = hackvigenere(ciphertext)

	if hackedMessage != None:
		print hackedMessage
	else:
		print 'failed'

if __name__ == '__main__':
	main()