#!/usr/bin/env python
import subprocess
import os
import socket


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is: " + hostname)
print("Your Computer IP Address is: " + IPAddr)

# Do not display output
FNULL = open(os.devnull, 'w')


def pingNetwork():
    network = IPAddr.split('.')
    starting_ip = input('Starting IP: ')
    ending_ip = input('Ending IP: ')

    for i in range(int(starting_ip), int(ending_ip)):

        try:
            subprocess.check_call(['ping', '-c', '1', f"{network[0]}.{network[1]}.{network[2]}." + str(i)], stdout=FNULL, stderr=FNULL)

        except (OSError, subprocess.CalledProcessError):

            print("[-] DOWN", f"{network[0]}.{network[1]}.{network[2]}." + str(i))
        else:

            print("[+] UP", f"{network[0]}.{network[1]}.{network[2]}." + str(i))


# pingNetwork()

my_network = ["ASUNTU", "beeplus", "zero", "PiHAT2", "ASUS10", "lego"]



def pingList():
    for device in my_network:
        # print(device + ".local")
        try:
            subprocess.check_call(['ping', '-c', '1', device + '.local'], stdout=FNULL, stderr=FNULL)

        except (OSError, subprocess.CalledProcessError):

            print("[-] DOWN {}".format(device))
        else:

            print("[+] UP {}".format(device))


pingList()