from scapy.all import *
import subprocess
import time
from datetime import datetime


def arp_capture(nb):
    """
    Capture and analyze ARP packets for a specified duration.
    """
    print(f"Capturing ARP packets for {nb} seconds.")
    sniff(
        prn=paquetHTTP,  # Callback function called for each captured packet
        filter='arp and src host ',  # Filter to capture only ARP packets from the specified source IP
        timeout=nb,
        iface="enp0s3"
    )


def paquetHTTP(paquet):
    """
    Analyse un paquet capturé pour extraire les informations ARP.
    """
    if ARP in paquet:
        arp = paquet[ARP]  # Store the object representing the ARP request

        # Extract information into a dictionary
        liste = []
        resultat = {
            "horloge": str(datetime.now()),
            "adresse_source": arp.hwsrc,
            "adresse_destination": arp.hwdst,
            "operation": arp.op
        }
        resultatfinal = "{}; {}; {}; {}".format(
            resultat["horloge"], resultat["adresse_source"], resultat["adresse_destination"], resultat["operation"]
        )
        liste.append(resultat)
        return resultatfinal