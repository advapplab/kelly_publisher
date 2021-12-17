#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import datetime
import os
import os.path
import sys

count = 0
HOST = '192.168.0.104'
PORT = int(sys.argv[1])
machine_num = sys.argv[2]
print(PORT)
#PORT = 8787
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)
exec_command = 'START /B python send_data.py ' + machine_num + ' &'
print(exec_command)
today = datetime.date.today()
filename = str(today) + str(PORT) + '_Vibration.txt'
print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection....')

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
            print('Machine: ' + machine_num +' The produce number:' , num)
            print('recv: ' + indata.decode())
            with open(filename, 'w') as f:
                f.write(str(num))
            os.system(exec_command)
        elif indata.decode() == 'y':
            print('Have People !!! ',count)
            count += 1
        


        #utdata = 'echo ' + indata.decode()
        #conn.send(outdata.encode())
