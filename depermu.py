# permutation cipher decoder
# author: Xing Yu
# fall 2017

import sys
import re
import itertools
import numpy  as np
from collections import defaultdict

############################### check input parameters ###########################
if len(sys.argv) != 3:
	print("usage: python3 depermu.py [cipher file name] [digram frequency file]")
	sys.exit()

################################ read and process cipher #########################
cipherfile = str(sys.argv[1])

m_max = 9

file = open(cipherfile, 'r')

text = file.read()

text = "".join(re.findall("[a-zA-Z]+", text))

file.close()

cipher = list(text)

############################# get ideal digram distribution #####################
digramfile = str(sys.argv[2])
ideal = defaultdict(list)

ideal = np.loadtxt(digramfile, dtype = np.float64, delimiter = ',')

# transform frequncy into probability
ideal = ideal/ideal.sum()

############################## out put distance and keys to a csv file ############
output = open("perout.csv", 'w')

############################## find the most appropriate permutation ##############
for m in range(2, m_max+1):
	for key in itertools.permutations(range(m)):
		colnum = m
		rownum = int((len(cipher) - len(cipher)%m)/m)

		blocks = cipher[0 : len(cipher) - len(cipher)%m]
		blocks = np.asarray(blocks, dtype = np.str)

		# break cipher in to columns based on the key
		blocks = np.resize(blocks, (rownum, colnum))

		# rearrange columns according to the key
		plain = blocks[:,key]

		# get digrams
		plain = np.resize(plain, (1, rownum*colnum))
		plain_prob = np.zeros((26,26), dtype = np.float64)

		# count digrams
		i = 0
		while(i < plain.size - 1):
			x = ord(plain[0,i]) - ord('A')
			y = ord(plain[0,i+1]) - ord('A')
			plain_prob[x,y] += 1.0
			i += 1

		# calculate probability
		plain_prob = plain_prob/plain_prob.sum()

		distance = np.sqrt(np.sum((plain_prob - ideal)**2))

		print(key)
		print(distance)

		output.write(str(distance))
		output.write(',')
		output.write(str(len(key)))
		output.write(',')
		for index in key:
			output.write(str(index))
			output.write(',')
		output.write('\n')

output.close()




