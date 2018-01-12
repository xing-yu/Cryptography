# hill cipher decoder
# author: Xing Yu
# fall 2017

import sys
import re
import itertools
import numpy  as np
from collections import defaultdict

############################### check input parameters ###########################
if len(sys.argv) != 2:
	print("usage: python3 dehill.py [cipher file name]")
	sys.exit()

cipherfile = str(sys.argv[1])

m = 2

file = open(cipherfile, 'r')

text = file.read()

text = "".join(re.findall("[a-zA-Z]+", text))

file.close()
#print(text)

cipher = list(text)

# guess: EB = HE MQ = IM
digrams = []
i = 0
while(i<len(cipher)-1):
	digrams.append(cipher[i]+cipher[i+1])
	print(cipher[i]+cipher[i+1], end = " [")
	print(ord(cipher[i])-ord('A'), end = ", ")
	print(ord(cipher[i+1])-ord('A'), end = "] ")
	if (ord(cipher[i])-ord('A'))%2==0 and (ord(cipher[i+1])-ord('A'))%2==0:
		print("N")
	else:
		print("Y")
	i = i+2

digramfre = {}
for digram in digrams:
	if digram in digramfre.keys():
		digramfre[digram] += 1
	else:
		digramfre[digram] = 1

for digram in digramfre.keys():
	print(digram, end = ": ")
	print(digramfre[digram])

############################### try match diagrams ##################################
digram1 = 'EB'
digram2 = 'RR'
#digram2 = 'RG'
#digram2 = 'PW'
digram3 = 'MQ'
digram4 = 'EG'
digram5 = 'SF'
candidates  = ['TH', 'AA', 'BB', 'CC', 'DD', 'EE','SS','FF', 'GG', 'HH', 'II', 'JJ', 'LL', 'MM', 'NN', 'OO', 'PP', 'QQ', 'RR', 'TT', 'UU', 'VV', 'WW', 'XX', 'YY', 'ZZ','KK','TT','HE', 'IN', 'ER', 'AN', 'RE', 'ED', 'ON', 'ES', 'ST', 'EN', 'AT', 'TO', 'NT', 'HA', 'ND', 'OU', 'EA', 'NG', 'AS', 'OR', 'TI', 'IS', 'ET', 'IT', 'AR', 'TE', 'SE', 'HI', 'OF']

b = np.array([[ord(digram1[0])-ord('A'),ord(digram1[1])-ord('A')],[ord(digram2[0])-ord('A'),ord(digram2[1])-ord('A')]])
binv = np.array([[9,1],[17,22]])
#binv = np.array([[12,11],[5,8]])
#binv = np.array([[20,5],[23,6]])
c = np.array([12,16])

t1 = np.array([4,6])
t2 = np.array([18,5])

for digram_c1 in candidates:
	for digram_c2 in candidates:
		if digram_c2 != digram_c1:
			a = np.array([[ord(digram_c1[0])-ord('A'),ord(digram_c1[1])-ord('A')],[ord(digram_c2[0])-ord('A'),ord(digram_c2[1])-ord('A')]])
			kinv = binv.dot(a)%26
			plain = c.dot(kinv)%26
			print(kinv)
			print(digram_c1)
			print(digram_c2)
			print(chr(plain[0]+ord('A')), end = "")
			print(chr(plain[1]+ord('A')))

			plain_t1 = t1.dot(kinv)%26
			print(chr(plain_t1[0]+ord('a')), end = "")
			print(chr(plain_t1[1]+ord('a')), end = "")

			plain_t2 = t2.dot(kinv)%26
			print(chr(plain_t2[0]+ord('a')), end = "")
			print(chr(plain_t2[1]+ord('a')))
############################### try key inverse #######################################
keyinv = np.array([[22,21],[23,24]])
for digram in digrams:
	v = np.array([ord(digram[0]) - ord('A'), ord(digram[1]) - ord('A')])
	plain = v.dot(keyinv)%26
	print(chr(plain[0]+ord('a')), end = "")
	print(chr(plain[1]+ord('a')), end = "")



