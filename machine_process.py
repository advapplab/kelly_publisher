#Argument

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("PORT") # 8787
parser.add_argument("machine_num") # 01

arguments = parser.parse_args()

PORT = arguments.PORT
machine_num = arguments.machine_num

#System command

import os

main_program = "start" + str(machine_num)

#Process

import psutil
import time

pid_num = ''

    
Process_Id_name = './Process_Id/' + 'Machine_' + str(machine_num) + '_Process_Id.txt'

print(Process_Id_name)

file_exist = False

try:
    with open(Process_Id_name, "r") as proc_infomation:
        proc_info = str(proc_infomation.readlines())
    file_exist = True
except:
    file_exist = False
    os.system(main_program)
    

proc_info = proc_info[2:-2]

run = False
for proc in psutil.process_iter():
    proc = str(proc)
    if proc_info in proc:
        run = True
        print(str(machine_num) + ' is running... close the cmd...')
if run == False:
    print(str(machine_num) + " isn't running. So we ready to Run")
    if file_exist:
        os.system(main_program)




