#!/usr/bin/python


g = 'g'
print ord(g)


n = 0
m = 0

def print_CHAR(n, m):
    chars = []
    for i in range(n,m):
        chars.append(chr(i))
    print chars
    return chars

#print_CHAR(32, 97)


def print_ASCII(arr):
    nums = []
    for i in arr:
        nums.append(ord(i))
    print nums

print_ASCII(print_CHAR(32, 97))
