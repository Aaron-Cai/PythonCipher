import itertools,re
import vigenereCipher, pyperclip, freqAnalysis, detectEnglish

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SILENT_MODE = False
NUM_MOST_FREQ_LETTERS = 4
MAX_KEY_LENGTH = 16
NONLETTERS_PATTERN = re.compile('[^A-Z]')


def findRepeatSequencesSpacings(message):
	seqSpacings = {}
	for seqLen in range(3,6):
		for seqStart in range(len(message) - seqLen):
			seq = message[seqStart:seqStart+seqLen]

			for i in range(seqStart+seqLen, len(message) - seqLen):
				if message[i:i+seqLen] == seq:
					if seq not in seqSpacings:
						seqSpacings[seq] = []
					seqSpacings[seq].append(i - seqStart)
	return seqSpacings

def getUsefulFactors(num):
	if num<2:
		return []
	factors = []
	for i in range(2,MAX_KEY_LENGTH+1):
		if num%i == 0:
			factors.append(i)
			factors.append(int(num/i))
	if 1 in factors:
		factors.remove(1)
	return list(set(factors))

def getItemAtIndexOne(x):
	return x[1]

def getMostCommonFactors(seqFactors):
	factorCounts = {}
	

def main():
	ciphertext = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, 
					izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce vmhsgohuqbo ox 
					kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm ocicwxfg jf "stscmilpy" 
					oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba 
					pz tzm roohwz at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. Pimifo Icmlv 
					Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm Supacg (GUKE) oo 
					Bdmfqclwg Bomk, Tzuhvif'a ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr 
					Vpt 8, lpq gzclqab mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp 
					o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts helpar 
					jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf 
					ohw Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl 
					Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a kbafzd-hzaumae 
					kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsv'e Qjmhcfwig Dincmalwdm 
					vt Eizqcekbqf Pnadqfnilg, ivzrw pq onsaafsy if bts yenmxckmwvf ca tzm 
					Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq 
					kmolm m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy 
					okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz, 
					kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdny'a tchokmjivlabk fzsmtfsy if 
					i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi 
					tzm Gbdtwl Wwigvwy. Vz aukqdoev bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl 
					uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs rdev qz 1954, xpsl whsm
					tow iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl
					lqhzreqzsy tzif vds vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk
					jqzdenmp vds vmmhc wsa mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo
					mb Dnlmdbzt uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz
					cafakuog pmjxwx ahwxcby gv nscadn at ohw Jdwoikp scqejvysit xwd 
					"hce sxboglavs kvy zm ion tjmmhzd." Sa at Haq 2012 i bfdvsbq azmtmd'g
					widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a 
					kbmhptgzk dvrvwz wa efiohzd."""	
	hackedMessage = hackVigenere(ciphertext)

	if hackedMessage != None:
		print hackedMessage
	else:
		print 'Failed to hack'




if __name__ == '__main__':
	main()