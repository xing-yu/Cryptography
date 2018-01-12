# Jacobi symbol
# Author: Xing Yu
# Fall 2017

########################## Jacobi Symbol #########################
def JacobiSymbol(m, n, c):
    #print(m)
    #print(n)
    #print(c)
    if n%2 != 0 and m%2 != 0 and m < n:             # property 4
        if n%4 == 3 and m%4 == 3:
            return JacobiSymbol(n, m, -1*c)
        else:
            return JacobiSymbol(n, m, 1*c)
    elif n%2 != 0 and m == 2:                       # property 2
        if n%8 == 1 or n%-8 == -1:
            return 1*c
        elif n%8 == 3 or n%-8 == -3:
            return (-1)*c
    elif n%2 != 0 and m%2 == 0 and m > 2:           # property 3
        if n%8 == 1 or n%-8 == -1:
            return JacobiSymbol(m/2, n, 1*c)
        elif n%8 == 3 or n%-8 == -3:
            return JacobiSymbol(m/2, n, -1*c)
    elif n%2 != 0 and m%2 != 0 and m > n:           # property 1
        return JacobiSymbol(m%n, n, c)
    else:
        return 0

######################### main ##################################
# (136/457)
result1 = JacobiSymbol(136, 457, 1)
# (34333/532789)
result2 = JacobiSymbol(34333, 532789, 1)
# (467827/112233441)
result3 = JacobiSymbol(467827, 112233441, 1)

print(result1)
print(result2)
print(result3)
