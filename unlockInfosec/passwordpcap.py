from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####
"""
Pcap file with 1 incorrect login and 1 correct login. We need to find the correct login.
"""


import re

def show_username_password():
    
    
    #Associate port 8000 with HTTP., (Default 80). Important BEFORE reading pcap.
    bind_layers(TCP, HTTP, dport=8000)
    bind_layers(TCP, HTTP, sport=8000)
    
    packets = rdpcap(recording_path)
    
    pat = 'username=(.*)&password=([^\s]+)'
    failedOnce = False
    
    for packet in packets:
        if (packet.haslayer(HTTP)):
            a = raw(packet[HTTP]).decode("ascii")
            match = re.search(pat, a)
            wrong = a.find("Invalid credentials.") != -1
            
            if match and failedOnce:
                print (match)
                
            if wrong:
                failedOnce = True
                        
            
    #raw(packets[2][HTTP]).decode("ascii")

show_username_password()

#I think should have checked straight forward the response for each match, instead of that failedOnce nasty thing because this solution only works for one wrong attpemt and then the correct login. 
