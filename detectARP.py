from scapy.all import *
import subprocess
import time



def get_mac(ip):
    command = ['ip', 'neigh', 'show', 'to', ip]
    output = subprocess.check_output(command, universal_newlines=True)
    lines = output.strip().split('\n')

    if lines:
        fields = lines[0].split()
        if len(fields) >= 5:
            return fields[4]

    return None

def compare_mac(ipa, ipb):
    mac_serveur = get_mac(ipa)
    mac_machine = get_mac(ipb)

    if mac_machine and mac_machine and mac_machine == mac_serveur:
        print("Hacker !")

    else:
        print("Les adresses MAC ne correspondentrepas.")

# Exemple d'utilisation
ip1 = "192.168.56.102"
ip2 = "192.168.56.101"

compare_mac(ip1, ip2)