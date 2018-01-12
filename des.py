# CSCI 55500
# Assignment 02
# Author: Xing Yu
# Fall 2017

import sys

####################### hexadeciaml to binary ###################
def hexToBin(hexStr):
    binStr = ''
    for char in hexStr:
        if char.isalpha():
            binPart = format(ord(char) - ord('A') + 10, '04b')
        else:
            binPart = format(ord(char) - ord('0'), '04b')
        binStr += binPart
    return binStr

####################### binary to hexadeciaml ###################
def binToHex(binStr):
    hexStr = ''
    block = ''
    for char in binStr:
        block += char
        if len(block) == 4:
            hexPart = hex(int(block,2))[-1:]
            if hexPart.isalpha():
                hexPart = hexPart.upper()
            hexStr += hexPart
            block = ''
    return hexStr
####################### left cyclic shift #######################
def leftCshift(binStr, p):
    return binStr[p:] + binStr[:p]

####################### key schedule function ###################
def keyGen(K, Nr, PC_1, PC_2):
    keys = []
    # reduce K from 64 bits into 56 bits
    K0 = ''
    for i in PC_1:
        K0 += K[i-1]
    # split K0 into C0 and D0
    Ci = K0[:int(len(K0)/2)]
    Di = K0[int(len(K0)/2):]
    for i in range(Nr):
        if i in [0, 1, 8, 15]:
            # left shift one position
            Ci = leftCshift(Ci, 1)
            Di = leftCshift(Di, 1)
        else:
            # left shift two positions
            Ci = leftCshift(Ci, 2)
            Di = leftCshift(Di, 2)
        Ki_prime = Ci + Di
        # reduce Ki_prime from 56 bits into 48 bits
        Ki = ''
        for j in PC_2:
            Ki += Ki_prime[j-1]
        keys.append(Ki)
    return keys

####################### expansion function ######################
# expand a 32 bit string to a 48 bit string
def expand(binStr, E):
    newStr = ''
    for i in E:
        newStr += binStr[i - 1]

    return newStr

####################### exclusive or function ###################
def exclusiveOr(binStr1, binStr2):
    if len(binStr1) != len(binStr2):
        print("exclusiveOr failed due to inequal length")
        sys.exit()
    resultStr = ''
    for i in range(len(binStr1)):
        if int(binStr1[i]) == int(binStr2[i]):
            char = '0'
        else:
            char = '1'
        resultStr += char

    return resultStr

####################### s box function ##########################
def sbox(binStr, S):        # input is 6 bits output is 4 bits
    rowStr = binStr[0] + binStr[-1]
    colStr = binStr[1:-1]
    row = int(rowStr, 2)
    col = int(colStr, 2)
    return format(S[row][col], '04b')

####################### permutation function ####################
def permuS(binStr, P):
    if len(binStr) != len(P):
        print("Permutation failed due to inequal length")
        print(len(binStr))
        print(len(P))
        sys.exit()

    resultStr = ''
    for i in P:
        resultStr += binStr[i-1]
    return resultStr

############ encryption right part function #####################
def encryptRightPart(key, rightHalf, S, P):  # plainStr is 48 bits
    newStr = exclusiveOr(rightHalf, key)
    block = ''      # 6 bits block
    i = 0           # s box counter
    resultStr = ''
    for b in newStr:    # sbox
        block += b
        if len(block) == 6:
            resultStr += sbox(block, S[i])
            i += 1
            block = ''
    resultStr = permuS(resultStr, P)    # permuate c

    return resultStr

####################### DES meta data ###########################
key0 = 'F20B319724A5C81D'
key0_test = '84EF48BD3FAAA3A8'

IV = '42767D9B9D683107'
IV_test = '27A1B6FCF7933158'

plainText = [
'5468697369736372',
'7970746F67726170',
'6879636F75727365']

IP = [
58,50,42,34,26,18,10,2,
60,52,44,36,28,20,12,4,
62,54,46,38,30,22,14,6,
64,56,48,40,32,24,16,8,
57,49,41,33,25,17,9,1,
59,51,43,35,27,19,11,3,
61,53,45,37,29,21,13,5,
63,55,47,39,31,23,15,7
]

IPinv = [
40,8,48,16,56,24,64,32,
39,7,47,15,55,23,63,31,
38,6,46,14,54,22,62,30,
37,5,45,13,53,21,61,29,
36,4,44,12,52,20,60,28,
35,3,43,11,51,19,59,27,
34,2,42,10,50,18,58,26,
33,1,41,9,49,17,57,25
]

PC_1 = [
57,49,41,33,25,17,9,
1,58,50,42,34,26,18,
10,2,59,51,43,35,27,
19,11,3,60,52,44,36,
63,55,47,39,31,23,15,
7,62,54,46,38,30,22,
14,6,61,53,45,37,29,
21,13,5,28,20,12,4]

PC_2 = [
14,17,11,24,1,5,
3,28,15,6,21,10,
23,19,12,4,26,8,
16,7,27,20,13,2,
41,52,31,37,47,55,
30,40,51,45,33,48,
44,49,39,56,34,53,
46,42,50,36,29,32]

E = [32,1,2,3,4,5,
4,5,6,7,8,9,
8,9,10,11,12,13,
12,13,14,15,16,17,
16,17,18,19,20,21,
20,21,22,23,24,25,
24,25,26,27,28,29,
28,29,30,31,32,1]

P = [
16,7,20,21,
29,12,28,17,
1,15,23,26,
5,18,31,10,
2,8,24,14,
32,27,3,9,
19,13,30,6,
22,11,4,25
]

S = [
[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],
[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],
[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],
[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],
[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],
[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]],
]

######################## DES encrypt function #####################
# generate keys
key0Bin = hexToBin(key0_test)
keys = keyGen(key0Bin, 16, PC_1, PC_2)
#print(key0Bin)
#print(keys)

cipher = []
IVBin = hexToBin(IV_test)                   # initial vector to binary
# encryption
for block in plainText:
    blockBin = hexToBin(block)              # plaintext hex to binary
    blockBin = exclusiveOr(blockBin, IVBin) # CBC mode
    blockBin = permuS(blockBin, IP)         # inital permutation
    #print(blockBin)
    for key in keys:                        # 16 rounds of substituion and permutation
        blockLeft = blockBin[:int(len(blockBin)/2)]
        #print(blockLeft)
        blockRight = blockBin[int(len(blockBin)/2):]
        #print(blockRight)
        tempBlock = expand(blockRight, E)   # expand right half into 48 bits
        #print(tempBlock)
        #print(key)
        tempBlock = encryptRightPart(tempBlock, key, S, P)  # encrypt the right part
        #print(tempBlock)
        tempBlock = exclusiveOr(blockLeft, tempBlock)       # exclusiveOr left with encrypted right part
        # swap left and right blocks
        blockLeft = blockRight
        blockRight = tempBlock
        blockBin = blockLeft + blockRight

    L16 = blockBin[:int(len(blockBin)/2)]
    R16 = blockBin[int(len(blockBin)/2):]
    blockBin = R16 + L16
    blockBin = permuS(blockBin, IPinv)      # reverse permutation
    IVBin = blockBin                        # update initial vector
    cipher.append(binToHex(blockBin))       # add cipher block to cipher

for block in cipher:
    print(block)

######################## DES decrypt function #####################
# generate keys
key0Bin = hexToBin(key0)
keys = keyGen(key0Bin, 16, PC_1, PC_2)
# reverse the round keys
keys.reverse()
#print(key0Bin)
#print(keys)

# prepare cipher
cipher = []
filename = "DES-ciphertext.txt"
f = open(filename, 'r')
for line in f:
    cipher.append(line.strip())

plain = []
IVBin = hexToBin(IV)                        # initial vector to binary
# encryption
for block in cipher:
    blockBin = hexToBin(block)              # plaintext hex to binary
    blockBin = permuS(blockBin, IP)         # inital permutation
    #print(blockBin)
    for key in keys:                        # 16 rounds of substituion and permutation
        blockLeft = blockBin[:int(len(blockBin)/2)]
        #print(blockLeft)
        blockRight = blockBin[int(len(blockBin)/2):]
        #print(blockRight)
        tempBlock = expand(blockRight, E)   # expand right half into 48 bits
        #print(tempBlock)
        #print(key)
        tempBlock = encryptRightPart(tempBlock, key, S, P)  # encrypt the right part
        #print(tempBlock)
        tempBlock = exclusiveOr(blockLeft, tempBlock)       # exclusiveOr left with encrypted right part
        # swap left and right blocks
        blockLeft = blockRight
        blockRight = tempBlock
        blockBin = blockLeft + blockRight

    L16 = blockBin[:int(len(blockBin)/2)]
    R16 = blockBin[int(len(blockBin)/2):]
    blockBin = R16 + L16
    blockBin = permuS(blockBin, IPinv)      # reverse permutation
    blockBin = exclusiveOr(blockBin, IVBin) # CBC mode
    IVBin = hexToBin(block)                 # update initial vector
    #plain.append(binToHex(blockBin))        # add cipher block to cipher
    plain.append(blockBin)

for block in plain:
    text = ''
    part = ''
    for i in block:
        part += i
        if len(part) == 8:
            #char = chr(int(part, 16))
            char = chr(int(part, 2))
            text += char
            part = ''
    print(text, end = '')

print('\n')
