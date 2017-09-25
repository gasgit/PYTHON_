#!/usr/bin/python

i = 1

while i <= 20:
    if( i % 2 ) == 0:
        i += 1
        continue
    if i == 15:
        break

    print  "ODD: ", i

    i += 1