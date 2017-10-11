#!/usr/bin/python


''' find odd occurrence in int array'''

A = [9,3,9,3,9,7,9]


print '********  XOR  *******'

def solution_XOR(A):

    res = 0
    for n in A:
        res = res ^ n
        print res
    print res
    return res

solution_XOR(A)


print '******* Counter ********'

from collections import Counter
def solution_collections(A):

    print type(Counter(A))
    print Counter(A)
    for i in Counter(A):
        if Counter(A)[i] % 2 == 1:
            print i
            return i

solution_collections(A)
