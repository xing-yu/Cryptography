# lfsr cipher decoder
# author: Xing Yu
# fall 2017

import sys
import re
import itertools
import numpy  as np
from collections import defaultdict

############################### check input parameters ###########################
if len(sys.argv) != 3:
	print("usage: python3 delfsr.py [cipher file name] [keyfile]")
	sys.exit()

cipherfile = str(sys.argv[1])

keyfile = str(sys.argv[2])

file = open(cipherfile, 'r')

text = file.read()

text = "".join(re.findall("[a-zA-Z]+", text))

file.close()
#print(text)

cipher = list(text)

pool1 = ['THE','AND','FOR','ARE','BUT','NOT','YOU','ALL','ANY','CAN','HAD','HER','WAS','ONE','OUR','OUT','DAY','GET','HAS','HIM','HIS','HOW','MAN','NEW','NOW','OLD','SEE','TWO','WAY','WHO','BOY','DID','ITS','LET','PUT','SAY','SHE','TOO','USE']
pool2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
part = ['H', 'H', 'I', 'S']

file  = open(keyfile, 'r')

for line in file:
	data = line.strip().split(',')
	c = []
	for i in data:
		c.append(int(i))

	c = np.asarray(c)

	for word in pool1:
		for letter in pool2:
			guess = word+letter
			#current = pool1+pool2

			guess = list(guess)
			initalv = []
			current = []
			keystream = []
			plain = []

			for i in range(4):
				key = (ord(part[i]) - ord(guess[i]))%26
				initalv.append(key)
				current.append(key)
				keystream.append(key)

			for i in range(len(cipher) - 4):
				newkey = (c.dot(np.asarray(current)))%26
				keystream.append(newkey)
				current.pop(0)
				current.append(newkey)

			for i in range(len(cipher)):
				pletter = (ord(cipher[i]) - ord('A') - keystream[i])%26 + ord('A')
				pletter = chr(pletter)
				plain.append(pletter.lower())

			print(c)
			print("".join(plain))

file.close()




