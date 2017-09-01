import unicodedata
import codecs 

def addSameSet(line, d, s):
	semicolumn1 = line.find(';')
	semicolumn2 = line.find(';',semicolumn1+1)
	lhs = line[0:semicolumn1].strip()
	lhs = chr(int(lhs,16))
	rhs = (line[semicolumn1+1:semicolumn2].strip()).split(' ')
	if len(rhs) == 1: 				# take one-by-one mapping from line
		rhs = chr(int(rhs[0],16)) 	#cast from str unicode codepoints into unicodes
		s.add(lhs)
		s.add(rhs)
		d[rhs[0]] = s 				# make these keys point to same set
		d[lhs] = s

def TakeUnicodesFromFile():
	filename = "confusables.txt"
	file = codecs.open(filename, "r",encoding='utf-8-sig', errors='ignore') #open file with unicode characters
	content = file.readlines()
	d = {}
	s = set()
	for line in content:
		if line != '\n':	#if there is not new line add same set
			addSameSet(line,d,s)
		else: 				# if there is new line create new set
			s= set()
	return d

def CompareWords(d,word1, word2):
	if len(word1) == len(word2):
		for i in range(len(word1)):
			ch = word1[i]
			ch2 = word2[i]
			if ch != ch2 and  ch2 not in d[ch]:
				#if chars are not same and the char is not in other homoglyph set
				return False
	else:
		return False
	return True



word1= input('Enter first word: ') 
word2 = input('Enter second word: ')


d = TakeUnicodesFromFile()


if word1==word2:
	print("They are already same!")
else:
	if CompareWords(d,word1,word2)  :
		print("there is homoglyph")
	else:
		print("They are different")
