#!/usr/bin/env python3

import subprocess

#show ifconfig info and ability to run shell cmds
#take interface down
subprocess.call("ifconfig eth0 down", shell=True)
#change mac address
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:66", shell=True)
#bring interface up to enable mac address change
subprocess.call("ifconfig eth0 up", shell=True)