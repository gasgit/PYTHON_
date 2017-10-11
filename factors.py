#!/usr/bin/python

print '******** Factors *******'

def factors(N):
    for i in range(1, N + 1):
        if N % i == 0:
            print i


factors(24)
