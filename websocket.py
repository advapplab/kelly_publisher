#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import datetime
import os
import os.path
import sys
import time
from datetime import timedelta
import datetime
from datetime import datetime
from datetime import date
import logging
from func_timeout import FunctionTimedOut, func_timeout
import psutil

count = 0
HOST = '192.168.0.104'
#HOST = '192.168.1.104'
PORT = int(sys.argv[1])
machine_num = sys.argv[2]
print(PORT)
#PORT = 8787
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)
exec_command = 'START /B python send_data.py ' + str(machine_num)
#exec_command = 'call python send_data.py ' + machine_num
#exec_command = 'python send_data.py ' + machine_num + ' &'
print(exec_command)
now_time = datetime.now()
now_time = now_time.strftime("%Y-%m-%d %H-%M-%S")
FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, filename = './' + str(machine_num) + '/Machine_' + str(machine_num) + " " + now_time + '.log', filemode='w', format=FORMAT)
print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection....')

'''
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
'''
pid_num = str(os.getpid())

proc_info = ""
for proc in psutil.process_iter():
    proc = str(proc)
    if 'pid='+pid_num+', name=\'python.exe\'' in proc:
        proc_info = str(proc)

Process_ID = './Process_Id/' + 'Machine_' + str(machine_num) + '_Process_Id.txt'
with open(Process_ID, "w") as text_file:
    text_file.write(str(proc_info))
    
def restart_program():
    #python = sys.executable
    #os.execl(python, python, * sys.argv)
    os._exit(0)

while True:
    conn, addr = s.accept()
    print('connected by ' + str(addr))
    while True:
        #indata = conn.recv(1024)
        try:
            indata = func_timeout(3600, lambda: conn.recv(1024))
            recv = indata.decode()
            #print(indata.decode())
        except FunctionTimedOut:
            logging.info('Machine: ' + str(machine_num) + ' restart')
            restart_program()
            
        if recv == 'x':
            #num += 1
            #os.popen(exec_command,'r',0)
            logging.info('Machine: ' + str(machine_num) + ' is working')
            print('Machine: ' + machine_num +' is working')
            print('recv: ' + indata.decode())
            '''
            with open(filename, 'w') as f:
                f.write(str(num))
            '''
            #os.system(exec_command)
            conn.close()
            os.system(exec_command)
            break
        '''
        if ConnectionResetError:
            conn.close()
            print('client closed connection.')
            break
        '''
        #utdata = 'echo ' + indata.decode()
        #conn.send(outdata.encode())
