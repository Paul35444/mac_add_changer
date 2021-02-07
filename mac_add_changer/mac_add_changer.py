#!/usr/bin/env python3

import subprocess
import optparse

#func to call to get user inputs/args
def get_arguments():
    parser = optparse.OptionParser()
#allow the user to use -i or --interface and store it under interface var; help option
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
#allow the user to us -m or --mac and store it to new_mac var; help option
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
#take options & args from user input
#changed to return to call everything from above code
    return parser.parse_args()

#func to call to change mac address
def change_mac(interface, new_mac):
#get user input from variable above
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
#show ifconfig info and ability to run shell cmds
#take interface down
    subprocess.call(["ifconfig", interface, "down"])
#change mac address
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#bring interface up to enable mac address change
    subprocess.call(["ifconfig", interface, "up"])

#get arguments from func above and store in options
(options, arguments) = get_arguments()
#call options from get_args func above and implement under change_mac func
change_mac(options.interface, options.new_mac)