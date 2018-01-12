# substitution cypher
# author: Xing Yu
# fall 2017

import sys
import re

if len(sys.argv) != 2:
	print("usage: python3 desub.py [filename]")
	sys.exit()

#################### key mapping###################
k = {}

k['T'] = 'e'
k['Z'] = 't'
k['Q'] = 'a'
k['L'] = 's'	
k['O'] = 'i'
k['F'] = 'n'
k['G'] = 'o'
k['K'] = 'r'
k['I'] = 'h'
k['S'] = 'l'
k['R'] = 'd'
k['E'] = 'c'
k['X'] = 'u'
k['D'] = 'm'
k['W'] = 'b'
k['H'] = 'p'
k['Y'] = 'f'
k['U'] = 'g'
k['V'] = 'w'
k['N'] = 'y'
k['C'] = 'v'
k['B'] = 'x'
k['A'] = 'k'	
k['M'] = '-'
k['P'] = 'j'
k['J'] = 'q'




filename = str(sys.argv[1])

file = open(filename, 'r')

text = file.read()

file.close()

text = "".join(re.findall("[a-zA-Z]+", text))

text = list(text)

file = open(filename, 'r')

originaltext = file.read()

file.close()

for letter in originaltext:
	if letter in k.keys():
		print(k[letter], end = "")
	else:
		print(letter, end = "")

print('\n')