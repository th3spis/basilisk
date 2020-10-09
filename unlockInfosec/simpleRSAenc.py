import math 

n = 33
e = 7
d = 3
public_key = (n, e)
private_key = (n, d)

def encrypt(m, public_key):
    return math.pow(m, public_key[1])%public_key[0]

def decrypt(c, private_key):
    return math.pow(c, private_key[1])%public_key[0]
