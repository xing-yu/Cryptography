# permutation cipher decoder
# author: Xing Yu
# fall 2017

import sys
import re
import itertools
import numpy  as np
from collections import defaultdict

############################### check input parameters ###########################
if len(sys.argv) != 2:
	print("usage: python3 depermu.py [cipher file name]")
	sys.exit()

################################ read and process cipher #########################
cipherfile = str(sys.argv[1])

m_max = 9

file = open(cipherfile, 'r')

text = file.read()

text = "".join(re.findall("[a-zA-Z]+", text))

file.close()

cipher = list(text)

#key = (7,5,2,3,4,0,8,6,1)
#key = (6,1,7,5,2,3,4,0,8)
key = (3,4,0,8,6,1,7,5,2)


m = len(key)
colnum = m
rownum = int((len(cipher) - len(cipher)%m)/m)

blocks = cipher[0 : len(cipher) - len(cipher)%m]
blocks = np.asarray(blocks, dtype = np.str)

# break cipher in to columns based on the key
blocks = np.resize(blocks, (rownum, colnum))

# rearrange columns according to the key
plain = blocks[:,key]
plain = np.resize(plain, (1, rownum*colnum))

for letter in plain[0]:
	print(letter.lower(), end='')

print('\n')
