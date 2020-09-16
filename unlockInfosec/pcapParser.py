from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore

#### USEFUL https://thepacketgeek.com/scapy/building-network-tools/part-04/
#### USEFUL https://scapy.readthedocs.io/en/latest/usage.html


def show_mac_address():
    packets = rdpcap(pcapPath.pcap)
    print(packets[2][Ether].src)
    print(packets[2][Ether].show()) #show everything (Ether)
    pass # print mac address

show_mac_address()
