# vigenere decoder
# author: Xing Yu
# CSCI55500
# fall 2017

import sys
import re
from collections import defaultdict

if len(sys.argv) != 2:
	print("usage: python3 devig.py [cipher file name]")
	sys.exit()

filename = str(sys.argv[1])

############################# determine keyword length###################
m_max = 10

file = open(filename, 'r')

text = file.read()

text = "".join(re.findall("[a-zA-Z]+", text))

file.close()
#print(text)

text = list(text)

#print(text)
for m in range(1,m_max+1):
	# check for each possible value of m
	y = defaultdict(list)
	for i in range(m):
		j = i
		while(j < len(text)):
			y[i].append(text[j])
			j += m
	#print(y)
	# calculate index of coicidence for each m
	Ic = []
	for substr in y.keys():
		frequency = {}
		for char in y[substr]:
			if char not in frequency.keys():
				frequency[char] = 1
			else:
				frequency[char] += 1
		p = 0
		for char in frequency.keys():
			p = p + (frequency[char]/len(y[substr]))**2
			p = round(p,3)

		Ic.append(p)

	print("Value of m is " + str(m))
	print("Indexes of coincidence are: ", end = "")
	print(Ic)
############################# determine the key #############################

m = 10

# ideal probability
p = {}
p[0] = 0.082
p[1] = 0.015
p[2] = 0.028
p[3] = 0.043
p[4] = 0.127
p[5] = 0.022
p[6] = 0.020
p[7] = 0.061
p[8] = 0.070
p[9] = 0.002
p[10] = 0.008
p[11] = 0.040
p[12] = 0.024
p[13] = 0.067
p[14] = 0.075
p[15] = 0.019
p[16] = 0.001
p[17] = 0.060
p[18] = 0.063
p[19] = 0.091
p[20] = 0.028
p[21] = 0.010
p[22] = 0.023
p[23] = 0.001
p[24] = 0.020
p[25] = 0.001 

y = defaultdict(list)
for i in range(m):
	j = i
	while(j < len(text)):
		y[i].append(text[j])
		j = j+ m

for substr in y.keys():
	M = []
	f = {}
	for k in range(26):
		f[k] = 0

	for char in y[substr]:
		k = ord(char) - ord('A')
		f[k] += 1

	for g in range(26):
		mg = 0
		for i in p.keys():
			mg += p[i]*f[(i+g)%26]/len(y[substr])
			mg = round(mg, 3)
		M.append(mg)

	print("i: ", end = "")
	print(substr)
	print(M)

########################### decode the cipher ####################
# based on the result, the keyword is 3,0,17,10,10,13,8,6,7,19
key = [3,0,17,10,10,13,8,6,7,19]	#the key is darkknight

# now we have the key, let's decode the cipher

file = open(filename, 'r')
cipher = file.read()
file.close()

m = 10
i = 0
for char in cipher:
	if ord(char) >= ord('A') and ord(char) <= ord('Z'):
		plain = ord(char) - ord('A') - key[i]
		if plain < 0:
			plain = plain + 26
		plain = plain + ord('a')
		print(chr(plain), end="")
		i = (i + 1)%10
	else:
		print(char, end="")

print('\n')




