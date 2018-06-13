#!/usr/bin/env python
import subprocess
import os

# Do not display output
FNULL = open(os.devnull, 'w')


def pingNetwork():
        network = input('Enter network i.e [192.168.2.0]: ')[0:-1]
        starting_ip = input('Starting IP: ')
        ending_ip = input('Ending IP: ')

        for i in range(int(starting_ip), int(ending_ip)):

            try:
                subprocess.check_call(['ping', '-c', '1', network + str(i)])   #, stdout=FNULL,stderr=FNULL)

            except (OSError, subprocess.CalledProcessError):

                print("[-] DOWN {}{}".format(network,i))
            else:

                print("[+] UP {}{}".format(network,i))


# pingNetwork()

my_network = ["ASUNTU", "beeplus", "zero", "PiHAT2", "ASUS10"]



def pingList():
    for device in my_network:
        # print(device + ".local")
        try:
            subprocess.check_call(['ping', '-c', '1', device + '.local'], stdout=FNULL,stderr=FNULL)

        except (OSError, subprocess.CalledProcessError):

            print("[-] DOWN {}".format(device))
        else:

            print("[+] UP {}".format(device))


pingList()