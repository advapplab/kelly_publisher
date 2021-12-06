#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import datetime
import os
import os.path

count = 0
HOST = '192.168.1.104'
PORT = 8787
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)
today = datetime.date.today()
filename = str(today) + '_Vibration.txt'
print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

if os.path.isfile(filename):
    with open(filename, 'r') as f:
        num = f.readline()
        num = int(num)
    print('open the log')
else:
    num = 0
    with open(filename, 'w') as f:
        f.write(str(num))
    print('cannt find the log')  


while True:
    conn, addr = s.accept()
    print('connected by ' + str(addr))

    while True:
        indata = conn.recv(1024)
        if len(indata) == 0: # connection closed
            conn.close()
            print('client closed connection.')
            break
        if indata.decode() == 'x':
            num += 1
            print('The produce number:' , num)
            print('recv: ' + indata.decode())
            with open(filename, 'w') as f:
                f.write(str(num))
        elif indata.decode() == 'y':
            print('Have People !!! ',count)
            count += 1
        


        #utdata = 'echo ' + indata.decode()
        #conn.send(outdata.encode())