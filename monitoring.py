#!/usr/bin/python
#
#  to run the script please istall nrpe firts (MacOs: brew install nrpe)

import subprocess
import os

def run_command(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (commnad_output, commnad_error) = p.communicate()
    return commnad_output, commnad_error

def run_nrpe(vm_ip,check):
    cmd_to_run = "check_nrpe --host {} --timeout 2 --command {}".format(vm_ip,check)
    cmd_out, cmd_error = run_command(cmd_to_run)
    return cmd_out


rows, columns = os.popen('stty size', 'r').read().split()
line= "-" * int(columns)

vm_list = {"postgres01": "192.168.0.30",
       "postgres02": "192.168.0.31",
       "nginx01": "192.168.0.10",
       "nginx02": "192.168.0.11",
       "odoo01": "192.168.0.20",
       "odoo02": "192.168.0.21",
       "odoo03": "192.168.0.22" }

checks_list = {"check_disk":"check_disk --args '-c 5 -w 15 -p / -u GB'",
               "check_load":"check_load --args '-c 2,2,2 -w 1,1,1'"
              }

running_vms = str(run_command("vagrant global-status --prune | awk '/running/ {print $2}' |tr '\n' ';' | sed 's/;$//'"))
print(line)

for vm in vm_list:
    vm_ip = vm_list[vm]
    if vm not in running_vms:
        print " {} is DOWN".format(vm)

for vm in vm_list:
    vm_ip = vm_list[vm]
    if vm in running_vms:
        print(line)
        for check in checks_list:
            check_to_run = checks_list[check]
            print "{} : {} -  {}".format(vm,check,run_nrpe(vm_ip,check_to_run)).strip()
