# CSCI 55500
# Assignment 02
# Author: Xing Yu
# Fall 2017

import math

########################### pollard p-1 ###########################
def pollardP(n, B):
    results = []
    a = 2
    for j in range(2, B+1):
        a = (a**j)%n
        d = math.gcd(a-1, n)
        if d > 1 and d < n:
            results.append(d)
    return set(results)

############### extended euclidean algorithm######################
def extendEu(a, b):
    a0 = a
    b0 = b
    t0 = 0
    t = 1
    s0 = 1
    s = 0
    q = a0//b0
    r = a0 - q*b0
    while r > 0:
        temp = t0 - q*t
        t0 = t
        t = temp
        temp = s0 - q*s
        s0 = s
        s = temp
        a0 = b0
        b0 = r
        q = a0//b0
        r = a0 - q*b0
    r = b0
    return [r,s,t]
############################# matrix #############################
NN = 68102916241556970724365932142686835003312542409731911391
bb = 36639088738407540894550923202224101809992059348223191299
B = 5555

M =  [
[' ','*','4','>','H','R','\\','f','o','x'],
['!','+','5','?','I','S',']','g','p','y'],
['\\',',','6','@','J','T','^','h','q','z'],
['#','-','7','A','K','U','_','i','r','{'],
['$','.','8', 'B','L','V','`','j','s','|'],
['%','/','9','C','M','W','a','k','t','}'],
['&','0',':','D','N','X','b','l','u','~'],
["'",'1',';','E','O','Y','c','m','v',' '],
['(','2','<','F','P','Z','d','n','w',' '],
[')','3','=','G','Q','[','e','\n',' ',' ']
]

#for row in M:
#    for char in row:
#        print(char)
#        print(ord(char))

text = "This homework"

encode = ''
for l in text:
    #print(l)
    #print(ord(l))
    found = False
    for i in range(10):
        if found == True:
            continue
        for j in range(10):
            if found == True:
                continue
            if M[i][j] == l:
                encode += str(i)
                encode += str(j)
                found = True

########################### factorize NN ###########################
#print(pollardP(NN,B))

p = 761059198034100157
#q = NN//p
q = 89484387571261623539483274324628239563

# check to see if q is prime
#print(pollardP(q, B))

############################ calculate private key #################
phi_n = (p-1)*(q-1)
print(math.gcd(phi_n, bb))
print(extendEu(phi_n, bb))

aa = 16462836914480784610286339451249581187707217172465562107
############################ decrypt cipher #########################
filename = 'RSA-ciphertext.txt'

f = open(filename, 'r')

#cipher  = []
plain = []

for block in f:
    xb = int(block.strip())
    xba = pow(xb, aa, NN)
    xba = str(xba)
    if len(str(xba))%2 != 0:
        xba = '0' + xba
    plain.append(xba)

for block in plain:
    part = ''
    for l in block:
        part += l
        if len(part) == 2:
            row = int(part[0])
            col = int(part[1])
            print(M[row][col], end = "")
            part = ''

print('\n')
