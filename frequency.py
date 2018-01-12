# count frequency of a text file
# author: Xing Yu
# fall 2017

import sys
import re

top = 10

if len(sys.argv) != 2:
	print("usage: python3 frequency.py [cipher file name]")
	sys.exit()

filename = str(sys.argv[1])

file = open(filename, 'r')

text = file.read()

text = "".join(re.findall("[a-zA-Z]+", text))

text = list(text)

# count and calculate probability for each letter
charset = set(text)
charset = sorted(charset)

prob = {}
for char in charset:
	prob[char] = text.count(char)/len(text)
	prob[char] = round(prob[char], 3)

items = [(v,k) for k, v in prob.items()]
items.sort()
items.reverse()

print(len(text))

print("################## letter count ######################")
i = 0
for item in items:
	if i < top:
		print(item[1], end = ': ')
		print(item[0])
		i += 1

# extract digram
digrams = {}
i = 1
for i in range(len(text)):
	if i < len(text) - 1:
		digram = text[i] + text[i+1]
		if digram not in digrams.keys():
			digrams[digram] = 1
		else:
			digrams[digram] += 1


items = [(v,k) for k, v in digrams.items()]
items.sort()
items.reverse()

print("################## digram count ############################")
i = 0
for item in items:
	if i < top:
		print(item[1], end = ': ')
		print(item[0])
		i += 1

# extract trigram
trigrams = {}
i = 1
for i in range(len(text)):
	if i < len(text) - 2:
		trigram = text[i] + text[i+1] + text[i+2]
		if trigram not in trigrams.keys():
			trigrams[trigram] = 1
		else:
			trigrams[trigram] += 1


items = [(v,k) for k, v in trigrams.items()]
items.sort()
items.reverse()

print("################## trigram count ############################")
i = 0
for item in items:
	if i < top:
		print(item[1], end = ': ')
		print(item[0])
		i += 1
