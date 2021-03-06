#!/usr/bin/env python3

import subprocess
import optparse
import re

#func to call to get user inputs/args
def get_arguments():
    parser = optparse.OptionParser()
#allow the user to use -i or --interface and store it under interface var; help option
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
#allow the user to us -m or --mac and store it to new_mac var; help option
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
#take options & args from user input
#changed to return to call everything from above code
    (options, arguments) = parser.parse_args()
#if statement to handle user errors/input
    if not options.interface:
        parser.error("ERROR: Please specify a useable interface, enter --help for additional info.")
    elif not options.new_mac:
        parser.error("ERROR: Please specify a MAC Address, enter --help for additional info.")
    return options

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

#func to get current mac address
def get_current_mac(interface):
#call options from get_args func above and implement under change_mac func
#change_mac(options.interface, options.new_mac)
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

#regex to search for MAC add \w = alphanumeric char
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
#print first occurence of result
        return mac_address_search_result.group(0)
    else:
#handle error
        print("[-] Could not read MAC address. Please check your input.")

#get arguments from func above and store in options
options = get_arguments()
#get interface entry and display
current_mac = get_current_mac(options.interface)
print ("Current Mac = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address was NOT changed. Please check your cmd line inputs.")
