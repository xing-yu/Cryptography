# CSCI 55500
# Assignment 05
# Author: Xing Yu
# Fall 2017

import numpy as np

#<<<<<<<<<<<<<<<<<<<<<<<< logrithmic signatures >>>>>>>>>>>>>>>>>>>>
#r_1 = 10
#r_2 = 9
#r_3 = 8
#r_4 = 7
#r_5 = 6
#r_6 = 5
#r_7 = 4
#r_8 = 3

r = [10,9,8,7,6,5,4,3]
m = [1,10,90,720,5040,30240,151200,604800]

pm = []
for i in range(len(r)):
	for j in range(r[i]):
		pm.append(j*m[i])

alpha = []
beta = []
f = open('PGM_logs.txt', 'r')	# read the file with logithamic signatures
for line in f:
	data = line.strip().split(',')
	alpha.append(list(map(int,data[0:10])))
	beta.append(list(map(int,data[10:])))

f.close()

#print(alpha)
#print(beta)

#print(len(alpha))
#print(len(beta))
#print(len(pm))
#<<<<<<<<<<<<<<<<<<<<<<<< composition function >>>>>>>>>>>>>>>>>>>>>
def composition(A, B):
    # A,B are permutation groups in standard notation
    # will return the result in standard notation
    if len(A) != len(B):
    	print("The length of A and B don't match")
    	return -1

    result = []
    for i in range(len(A)):
    	result.append(B[A[i]-1])

    return result

#print(composition([3,2,1,5,4], [2,5,4,3,1]))
#print(composition([2,5,4,3,1], [3,2,1,5,4]))
#<<<<<<<<<<<<<<<<<<<<<<<< inverse function >>>>>>>>>>>>>>>>>>>>>>>>>
def inverse(A):
    # A is a permuation group in standard notation
    # will return A inverser in standard notation
    result = []
    for i in range(len(A)):
    	result.append(0)

    for i in range(len(A)):
    	result[A[i]-1] = i+1

    return result

#print(inverse([5,1,4,2,3]))
#<<<<<<<<<<<<<<<<<<<<<<<< match function >>>>>>>>>>>>>>>>>>>>>>>>>>>
def match(A, group, ri):
    # match A to a permutation in block ri in group
    upper_bound = 0
    for i in range(ri):
    	upper_bound += r[i]

    lower_bound = upper_bound - r[ri-1]

    for i in range(lower_bound, upper_bound):
    	if(A[ri-1] == group[i][ri-1]):
    		return [group[i], i]
    		break

#<<<<<<<<<<<<<<<<<<<<<<<< decomposition function >>>>>>>>>>>>>>>>>>>
def lamda_inv(N, pm):
	# decompose a number based on the pm values
	# return a binary vector corresponding to the pm vector
	result = []
	for i in range(len(pm)):
		result.append(0)

	n = len(pm) - 1
	j = len(r) - 1
	while j >= 0:
		i = 0
		found = -1
		while i < r[j]:
			if N >= pm[n-i] and found == -1:
				result[n-i] = 1
				N = N - pm[n-i]
				found = 1
			i += 1
		n = n - r[j]
		j = j - 1

	return result

#<<<<<<<<<<<<<<<<<<<<< PGM main function >>>>>>>>>>>>>>>>>>>>>>>>>>
def PGM(p,pm,alpha,beta,r):
	# p: plain text, an integer
	# pm: the vector of all p_i*m_i
	# alpha: the array of alpha permutation in the lograthmic signatures
	# beta: the array of beta permutaion in the lograthmic signatures
	# r: vector of r values for each block of logs
	# return an integer
	binaryVector = lamda_inv(p, pm)
	
	#print(pm)
	#print(binaryVector)
	#print(p)
	#x = np.asarray(binaryVector, dtype = np.int)
	#y = np.asarray(pm, dtype = np.int)
	#print(x.dot(y))
	
	inital_set = -1						# marker of the first permutation
							
	# the composition of all permutations correspond to plaintext
	result = []
	j = len(binaryVector) - 1
	while j >= 0:
		if binaryVector[j] == 1:
			if inital_set == -1:
				result = alpha[j]
				inital_set = 1
			else:
				result = composition(result, alpha[j])
		j = j - 1

	cipher = 0
	for i in range(len(r)):				# find corresponding permuations in beta
		match_result = match(result, beta, i+1)
		cipher += pm[match_result[1]]
		#print(result)
		#print(match_result[1])
		#print(match_result[0])
		result = composition(result, inverse(match_result[0]))

	return cipher

#<<<<<<<<<<<<<<<<<<< The encoding matrix >>>>>>>>>>>>>>>>>>>>>>>>>>>>
encodingVector = [
' ', '!', '"', '#', '$', '%', '&', "'", '(', ')',
'*', '+', ',', '-', '.', '/', '0', '1', '2', '3',
'4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
'>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[',
'\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e',
'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
'z', '{', '|', '}', '~', '\n', '\r']

#<<<<<<<<<<<<<<<<<<< cipher preprocess >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# turn ciphertext into indices
f = open('PGM_ciphertext.txt', 'r')

indices = []

for line in f:
	for char in line:
		# print(encodingVector.index(char), end = ' ')
		if char != '\n' and char != '\r':
			#print(encodingVector.index(char), end = ' ')
			indices.append(encodingVector.index(char))

	#print('\n')
f.close()

#<<<<<<<<<<<<<<<<<<  main script >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# decrypt the cipher

M = 95*95*95
seed = 2000

y = []
part = []
for element in indices:
	if len(part) == 3:
		#print(part, end = ' ')
		y.append(part[0]*95*95 + part[1]*95 + part[2])
		part = []
		part.append(element)
	else:
		part.append(element)

x = []
for i in range(len(y)):
	p = seed + i
	k = PGM(p,pm,alpha,beta,r)
	x.append((y[i]-k)%M)

for xi in x:
	index1 = int(xi/(95*95))
	index2 = int((xi - index1*95*95)/95)
	index3 = xi - index1*95*95 - index2*95
	print(encodingVector[index1], end = '')
	print(encodingVector[index2], end = '')
	print(encodingVector[index3], end = '')

print('\n')

