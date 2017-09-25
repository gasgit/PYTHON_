#!/usr/bin/python

from socket import *

host = '192.168.0.10'
min_p = 1
max_p = 65000

def scan_host(host, port, r_code = 1 ):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        c = s.connect_ex((host, port))
        if c == 0:
            r_code = c
        s.close()
    except Exception, e: 
        print e
    return r_code

def scan_target_host():
    for port in range(min_p, max_p):
        try:
            res = scan_host(host, port)
            if res == 0:
                print "Port %d: Open" %(port)
        except Exception, e: 
            pass



scan_target_host()