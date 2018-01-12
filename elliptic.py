# Assignment 03
# CSCI55500
# Xing Yu
# Fall 2017
# Question 04

#<<<<<<<<<<<<<<<<<<<<<<<< extendEu >>>>>>>>>>>>>>>>>>>>>>>>>>>
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
    #return [r,s,t]
    return t

#<<<<<<<<<<<<<<<<<<<<<<<< calculate points on curve >>>>>>>>>>
Z = 1039
ptcount = 0
x_max = 0
for i in range(Z):
    x = i+1
    y2 = x**3 + x + 6
    a = y2%Z
    if pow(a, int((Z-1)/2), Z) == 1:
        ptcount += 2
        x_max = x
print(ptcount)
print(x_max)
# 1008 + O
#<<<<<<<<<<<<<<<<<<< finding the lexically largest point >>>>>
y2 = x_max**3 + x_max + 6
a = y2%Z
y_1 = pow(a, int((Z+1)/4), Z)
y_2 = -pow(a, int((Z+1)/4))%Z
print(x_max, y_1, y_2)
# 1038 2 1037
#<<<<<<<<<<<<<<<<<< check if points on curve >>>>>>>>>>>>>>>>>>
x = 1014
y = 291
a = x**3 + x + 6
a = a%Z
if (y**2)%Z == a:
    print("yes")
else:
    print("no")
# no
#<<<<<<<<<<<<<<<<<< calculate lamda >>>>>>>>>>>>>>>>>>>>>>>>>>>
def computeLamda(x_1, y_1, x_2, y_2, a, p):
    if x_1 == x_2 and y_1 == y_2:
        lam = (x_1*x_1*3 + a)*extendEu(p, (2*y_1)%p)
        lam = lam%p
    else:
        lam = (y_2 - y_1)*extendEu(p, (x_2 - x_1)%p)
        lam = lam%p
    return lam

#<<<<<<<<<<<<<<<<<<< add points >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def addpoints(x_1, x_2, y_1, y_2, p, a):
    if x_1 == x_2 and y_1 == -1*y_2:
        return 0
    else:
        lam = computeLamda(x_1, y_1, x_2, y_2, a, p)
        x_3 = lam*lam - x_1 - x_2
        x_3 = x_3%p
        y_3 = lam*(x_1 - x_3) - y_1
        y_3 = y_3%p
    return [x_3, y_3]

#<<<<<<<<<<<<<<<<<<< ElGamal encryption >>>>>>>>>>>>>>>>>>>>>>>>
alpha = [799,790]
beta = [385,749]
K = 100
plain = [575,419]
a = 1
Z = 1039
# cipher = plain*beta^a
# additive
# cipher = plain + a*beta

Kalpha = alpha
for i in range(K-1):
    Kalpha = addpoints(Kalpha[0], alpha[0], Kalpha[1], alpha[1], Z, a)

Kbeta = beta
for i in range(K-1):
    Kbeta = addpoints(Kbeta[0], beta[0], Kbeta[1], beta[1], Z, a)

cipher = addpoints(Kbeta[0], plain[0], Kbeta[1], plain[1], Z, a)

print(Kalpha, cipher)
#[873, 233] [963, 817]

#<<<<<<<<<<<<<<<<<<< decrypt private key >>>>>>>>>>>>>>>>>>>>>>>
aalpha = alpha
key = 1
for i in range(10000):
    aalpha = addpoints(aalpha[0], alpha[0], aalpha[1], alpha[1], Z, a)
    key += 1
    #print(aalpha)
    if aalpha[0] == 385 and aalpha[1] == 749:
        print(aalpha)
        print(key)
        break

cipher = [234,14]
alpha = [873,233]
Kalpha = alpha
for i in range(key-1):
    Kalpha = addpoints(Kalpha[0], alpha[0], Kalpha[1], alpha[1], Z, a)

y_inv = Kalpha[0]**3 + Kalpha[0] + 6
y_inv = y_inv%Z
y_1 = pow(y_inv, int((Z+1)/4), Z)
y_2 = -pow(y_inv, int((Z+1)/4))%Z

if y_1 == Kalpha[1]:
    Kalpha[1] = y_2
else:
    Kalpha[1] = y_1

plain = addpoints(cipher[0], Kalpha[0], cipher[1], Kalpha[1], Z, a)
print(plain)

# key = 939
# plain = 319,784
#<<<<<<<<<<<<<<<<<<<<<< key exchange >>>>>>>>>>>>>>>>>>>>>>>>>>>>
alpha = [818, 121]
aa = 1
aalpha = alpha
for i in range(10000):
    aalpha = addpoints(aalpha[0], alpha[0], aalpha[1], alpha[1], Z, a)
    aa += 1
    #print(aalpha)
    if aalpha[0] == 199 and aalpha[1] == 72:
        print(aalpha)
        print(aa)
        break

bb = 1
balpha = alpha
for i in range(10000):
    balpha = addpoints(balpha[0], alpha[0], balpha[1], alpha[1], Z, a)
    bb += 1
    #print(aalpha)
    if balpha[0] == 815 and balpha[1] == 519:
        print(balpha)
        print(bb)
        break

# aa = 516 bb = 1001

ab = (516*1001)%Z
abalpha = alpha
for i in range(ab - 1):
    abalpha = addpoints(abalpha[0], alpha[0], abalpha[1], alpha[1], Z, a)

print(abalpha)

# 772, 204
