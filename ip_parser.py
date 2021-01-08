#!/usr/bin/env python3

#Accepts ips or ip ranges (ip with netmask) as arguments and returns a list of ipaddress.IPv4Address objects

import sys
import re
import socket
import ipaddress

listoncio = []

#With a little effort
def parse_ips(argumensio):
	global listoncio
	try:
		t = ipaddress.ip_network(argumensio, strict=True)
		net_str = str(t)
		print("\nNetwork is: " + net_str + "\n")
		single = re.match(r".*\/32", net_str)
		if single:
			ip = ipaddress.ip_address(net_str[:-3])
			listoncio.append(ip)
		else:
			for ip in t.hosts():
				listoncio.append(ip)
			#print(t.hosts().exploded)
	except Exception as e:
		print(e)

for arg in sys.argv[1:]:
	parse_ips(arg)

print("Final list: ")
print(listoncio)


"""
#With regex
aa = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", sys.argv[1])
if aa:
	print("\nIP is ", sys.argv[1])
else:
	print(sys.argv[1] + " is not an ip\n")

#With socket
try:
	socket.inet_aton(sys.argv[1])
	print()
	print(socket.inet_aton(sys.argv[1]))
except  Exception as e:
	print(e)
  """
