import unicodedata
import codecs 

def CheckMaps(maps, inputs, index):
	i=0
	cont= True
	while cont and index[1]+len(maps)<len(inputs[1])+1 and i<len(maps):
		char2= ('%04x' % ord(inputs[1][index[1]+i])).upper()
		if char2!=maps[i]:
			cont =False
		i+=1
	if cont and (index[1]+len(maps)) <= len(inputs[1]):
		index[1]+=i
		index[0]+=1

	return cont

def SearchInMaps(dicts,inputs,index,ordofChar):
	check = False
	for key, value in dicts.items():
		if value[0] == ordofChar and index[0]+len(value)<=len(inputs[0]) and key == ('%04x' % ord(inputs[1][index[1]])).upper():
			i = 1
			c = True
			while i < len(value)  and c:
				if value[i] == ('%04x' % ord(inputs[0][index[0]+i])).upper():
					c = True
				else: 
					c=False
				i+=1
			if c and i == len(value):
				index[0]+=i
				index[1]+=1
				return True

#Precondition: Takes line which contains unicode macthing, 2 word, 
#character and index of character
#Postcondition: Check all possible line conditions returns True if matching find
def SearchForChar(dicts,inputs,index,ch):
	check = True
	ordofChar = ('%04x' % ord(ch)).upper()

	if  ordofChar in dicts:	# if char code  is in left side
		check = CheckMaps(dicts[ordofChar],inputs,index) # compare second word according to maps chars
	else:
		check = SearchInMaps(dicts,inputs,index,ordofChar)

	return check 

#Precondition: Takes two string, find possible homoglyph
#Postcondition: Returns a boolean value: if there is a homoglyph returns True
#										 else returns false
def iterateOnWords(dictionary,inputs):
	index = [0,0]
	Status = True
	while index[0] < len(inputs[0]) and Status:	#iterate over input1
		if index[1]< len(inputs[1]) and inputs[0][index[0]] != inputs[1][index[1]] : #check is this same chars
			if not SearchForChar(dictionary,inputs,index,inputs[0][index[0]]):
				Status = False
				return Status

		else:
			index[0]+=1
			index[1]+=1
	if index[1] != len(inputs[1])  or index[0] != len(inputs[0]) :
		Status = False

	return Status

def compareInputs(inputs):
	if len(inputs[0])>len(inputs[1]):
		temp = inputs[0]
		inputs[0]=inputs[1]
		inputs[1]= temp

def TakeUnicodesFromFile():
	filename = "confusables.txt"
	file = codecs.open(filename, "r",encoding='utf-8', errors='ignore') #open file with unicode characters
	content = file.readlines()
	dictionary = {}
	for line in content:
		semicolumn1 = line.find(';')
		semicolumn2 = line.find(';',semicolumn1+1)
		dictionary[line[0:semicolumn1].strip()] = (line[semicolumn1+1:semicolumn2].strip()).split(' ')
	return dictionary

inputs = []
"""
inputs[0] = input('Enter first word: ') 
inputs[1] = input('Enter second word: ')
"""
inputs = ["a(H)","aa🄗"]
dictionary = TakeUnicodesFromFile()

if inputs[0]==inputs[1]:
	print("They are already same!")
else:
	compareInputs(inputs)
	if iterateOnWords(dictionary,inputs):
		print("there is homoglyph")
	else:
		print("They are different")