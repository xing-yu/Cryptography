# decrypt a LFSR cipher version 2
# author: Xing Yu
# CSCI55500
# fall 2017

import sys
import re
import itertools
import numpy  as np
from collections import defaultdict

#guess = "THESTHES"
#part = "ZVOIXVIA"
#cipher = "ZVOIXVIASEZIJGBFUBXEHXMAWBLIJZQJSCZLNMXSPWKYZXAUFCJBDQMXKLBWOOCGEKYGOIRUGURIMLYMSHIIIPYGVZGTIEBPUNECTSDGXIOFBCDIDBSBBBMLHSSZXOOAQCQQCJXHTYFKKCTFYVVKJDURMOYJTWQQAQNBOQINJSX"
cipher = "UFCJBDQMXKLBWOOCGEKYGOIRUGURIMLYMSHIIIPYGVZGTIEBPUNECTSDGXIOFBCDIDBSBBBMLHSSZXOOAQCQQCJXHTYFKKCTFYVVKJDURMOYJTWQQAQNBOQINJSX"
part = "UFCJBDQM"
#guess = "SANDTHES"
'''
pool = ['THE','AND','FOR','ARE','BUT','NOT','YOU','ALL','ANY','CAN','HAD','HER','WAS','ONE','OUR','OUT','DAY','GET','HAS','HIM','HIS','HOW','MAN','NEW','NOW','OLD','SEE','TWO','WAY','WHO','BOY','DID','ITS','LET','PUT','SAY','SHE','TOO','USE']

for word1 in pool:
	for word2 in pool:
		guess = 'S' + word1 + word2 + 'S'
		for c1 in range(26):
			for c2 in range(26):
				for c3 in range(26):
					for c4 in range(26):
						#ivector_list = [6, 14, 10, 16]
						ivector_list = []
						iv = []
						keystream = []
						current = []

						for i in range(4):
							key = (ord(part[i]) - ord(guess[i]))%26
							ivector_list.append(key)
							keystream.append(key)
							current.append(key)
							iv.append(key)

						iv = np.asarray(iv)

						c = []
						c.append(c1)
						c.append(c2)
						c.append(c3)
						c.append(c4)
						#print(c)
						c = np.asarray(c)

						ivector = np.asarray(ivector_list)
						newkey = int(round(c.dot(ivector),0))%26
						#print(newkey)
						if chr((newkey + ord(guess[4]) - ord('A'))%26 + ord('A')) != part[4]:
							continue

						ivector_list.pop(0)
						ivector_list.append(newkey)

						ivector = np.asarray(ivector_list)
						newkey = int(round(c.dot(ivector),0))%26
						#print(newkey)
						if chr((newkey + ord(guess[5]) - ord('A'))%26 + ord('A')) != part[5]:
							continue

						ivector_list.pop(0)
						ivector_list.append(newkey)

						ivector = np.asarray(ivector_list)
						newkey = int(round(c.dot(ivector),0))%26
						#print(newkey)
						if chr((newkey + ord(guess[6]) - ord('A'))%26 + ord('A')) != part[6]:
							continue

						ivector_list.pop(0)
						ivector_list.append(newkey)

						ivector = np.asarray(ivector_list)
						newkey = int(round(c.dot(ivector),0))%26
						#print(newkey)
						if chr((newkey + ord(guess[7]) - ord('A'))%26 + ord('A')) != part[7]:
							continue

						#print(c)
						cipher = list(cipher)
						plain = []
						for i in range(len(cipher)-4):
							newkey = int(round(c.dot(np.asarray(current)),0))%26
							keystream.append(newkey)
							current.pop(0)
							current.append(newkey)
						for i in range(len(cipher)):
							letter = chr((ord(cipher[i]) - ord('A') - keystream[i])%26 + ord('A'))
							plain.append(letter.lower())

						print("".join(plain))

################################ found the guess ##############################						
'''
guess = 'SNOTTHES'
for c1 in range(26):
	for c2 in range(26):
		for c3 in range(26):
			for c4 in range(26):
				#ivector_list = [6, 14, 10, 16]
				ivector_list = []
				iv = []
				keystream = []
				current = []

				for i in range(4):
					key = (ord(part[i]) - ord(guess[i]))%26
					ivector_list.append(key)
					keystream.append(key)
					current.append(key)
					iv.append(key)

				c = []
				c.append(c1)
				c.append(c2)
				c.append(c3)
				c.append(c4)
				#print(c)
				c = np.asarray(c)

				ivector = np.asarray(ivector_list)
				newkey = int(round(c.dot(ivector),0))%26
				#print(newkey)
				if chr((newkey + ord(guess[4]) - ord('A'))%26 + ord('A')) != part[4]:
					continue

				ivector_list.pop(0)
				ivector_list.append(newkey)

				ivector = np.asarray(ivector_list)
				newkey = int(round(c.dot(ivector),0))%26
				#print(newkey)
				if chr((newkey + ord(guess[5]) - ord('A'))%26 + ord('A')) != part[5]:
					continue

				ivector_list.pop(0)
				ivector_list.append(newkey)

				ivector = np.asarray(ivector_list)
				newkey = int(round(c.dot(ivector),0))%26
				#print(newkey)
				if chr((newkey + ord(guess[6]) - ord('A'))%26 + ord('A')) != part[6]:
					continue

				ivector_list.pop(0)
				ivector_list.append(newkey)

				ivector = np.asarray(ivector_list)
				newkey = int(round(c.dot(ivector),0))%26
				#print(newkey)
				if chr((newkey + ord(guess[7]) - ord('A'))%26 + ord('A')) != part[7]:
					continue

				print(",".join(map(str,c)))
				cipher = list(cipher)
				plain = []
				for i in range(len(cipher)-4):
					newkey = int(round(c.dot(np.asarray(current)),0))%26
					keystream.append(newkey)
					current.pop(0)
					current.append(newkey)
				for i in range(len(cipher)):
					letter = chr((ord(cipher[i]) - ord('A') - keystream[i])%26 + ord('A'))
					plain.append(letter.lower())

				#print("".join(plain))


		