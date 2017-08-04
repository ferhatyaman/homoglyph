import unicodedata
import codecs 

def makeSets(d, lhs, rhs):
	if len(rhs) == 1:
		rhs = chr(int(rhs[0],16))
		if rhs in d:
			s = d[rhs] 
			s.add(lhs)
			d[lhs] = s
		else:
			s = set()
			s.add(lhs)
			s.add(rhs)
			d[rhs] = s
			d[lhs] = s	


def TakeUnicodesFromFile():
	filename = "confusables.txt"
	file = codecs.open(filename, "r",encoding='utf-8-sig', errors='ignore') #open file with unicode characters
	content = file.readlines()
	d = {}
	for line in content:

		if line != '\n':
		
			semicolumn1 = line.find(';')
			semicolumn2 = line.find(';',semicolumn1+1)
			lhs = line[0:semicolumn1].strip()
			lhs = chr(int(lhs,16))
			rhs = (line[semicolumn1+1:semicolumn2].strip()).split(' ')
			makeSets(d, lhs, rhs)
			
	return d

def CompareWords(d,words):
	check = True
	i = 0
	while i <len(words[0]) and check:
		ch = words[0][i]
		ch2 = words[1][i]
		if  ch !=ch2 :
			check = ch2 in d[ch] 
		i+=1
	return check


# safafsklfaj
inputs = []
"""
inputs[0] = input('Enter first word: ') 
inputs[1] = input('Enter second word: ')
"""
inputs = ["wikipedia.org","wikipediа.org"]
d = TakeUnicodesFromFile()

if inputs[0]==inputs[1]:
	print("They are already same!")
else:
	if CompareWords(d,inputs):
		print("there is homoglyph")
	else:
		print("They are different")