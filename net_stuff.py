#!/usr/bin/python


''' scan ports on given ip on local network to show which are open '''

from socket import *
from struct import *

# host addr of machine to scan
host = '192.168.0.10'
# min port no
min_p = 1
# max port no
max_p = 5000

# function connect host
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
# function iterate range ports
def scan_target_ports():
    for port in range(min_p, max_p):
        try:
            res = scan_host(host, port)
            if res == 0:
                print "Port %d: Open" %(port)
        except Exception, e:
            print e


# check out protocols & packets
def test_socket():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
   # s = socket.socket(socket.AF_INET, socket.SOCK_RAW,socket.IPPROTO_UDP)
   # s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW,socket.ntohs(0x0003))


    while True:
        pkt =  s.recvfrom(3306)
        #print pkt

        pkt = pkt[0]
        #print pkt
        # ip header 20 bytes
        ip_header = pkt[0:20]

        ip_h = unpack('!BBHHHBBH4s4s', ip_header)
        print ip_h

        v_ihl = ip_h[0]
        print v_ihl
        # bit shift >> 4 palces to the right
        # eg 69. 01000101 >> 4 result binary 100, decimal val 4
        version = v_ihl >> 4
        print 'Version: ' + str(version)
        




scan_target_ports()
test_socket()
