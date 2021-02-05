#!/usr/bin/env python3

import subprocess

interface = input("Network Interface: ")
new_mac = input("New MAC Address: ")

#get user input from variable above
print("[+] Changing MAC address for " + interface + " to " + new_mac)

#show ifconfig info and ability to run shell cmds
#take interface down
subprocess.call(["ifconfig " + interface + " down"])
#change mac address
subprocess.call(["ifconfig " + interface + " hw ether " + new_mac])
#bring interface up to enable mac address change
subprocess.call(["ifconfig " + interface + " up"])

