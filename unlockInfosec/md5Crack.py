#!/usr/bin/env python3

import hashlib
import itertools
import string

def weak_md5(s):
     return hashlib.md5(s).digest()[:5]

def find_collisions():
    hashes = {}
    chars = chars = string.ascii_letters + '1234567890'
    
    
    #Loop for trying with different lengths i
    for i in range(40):
        for item in itertools.product(chars, repeat=i):
            newItem = ''.join(item) 
            newHash = weak_md5(newItem)
            if newHash in hashes:
                print('Found the next strings with same hash: \n')
                print(newItem, hashes[newHash])
                return (newItem, hashes[newHash])
            else: 
                hashes[newHash] = newItem 


find_collisions()
