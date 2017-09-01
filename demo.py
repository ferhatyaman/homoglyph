from homoglyph import *
from multiprocessing import Process, Pool
from readTwitterData import *
from itertools import combinations 
import os, time

def doCompare(domains):
	similar = list()
	glyph = Homoglyph()
	for tuples in combinations(domains,2):
		if glyph.compare(tuples[0],tuples[1]):
			similar.append(tuples)
	return similar


def openFile(filename,domains):
	lineDomain = TwitterData()
	file = open(filename,'r')
	for line in file:
		dmn = lineDomain.readDomains(line)
		if dmn != None:
			if dmn in domains.keys():
				domains[dmn] += 1
			else:
				domains[dmn] = 1

def openFolder(domains):
	count = 0
	for filename in os.listdir('./txt'):
		start_time = time.time()
		filename = './txt/' + filename
		openFile(filename,domains)
		print(len(domains))
		print ('{}. file  {}  Time taken: {}'.format(count,filename,time.time() - start_time))
		count+=1

"""
if __name__ == '__main__':
	start_time = time.time()
	domains = dict()
	result = list()
	openFolder(domains)
	
	#openFile("./txt/Gardenhose.1492337690",domains)
	print ('Done! Time taken: {}'.format(time.time() - start_time))
	print(len(domains))
	result = doCompare(domains.keys())
	print ('Done! Time taken: {}'.format(time.time() - start_time))
"""
"""
domains = dict()
openFile("./txt/Gardenhose.1492337690",domains)
"""
start_time = time.time()
domains = dict()
result = list()
openFolder(domains)
print ('Done! Time taken: {}'.format(time.time() - start_time))
result = doCompare(domains.keys())
print ('Done! Time taken: {}'.format(time.time() - start_time))
f = open("output.txt","w")
for tuples in result:
	f.write("{}: occurs {} times, {}:occurs {} times \n".format(tuples[0],domains[tuples[0]],tuples[1],domains[tuples[1]]))
print(result)