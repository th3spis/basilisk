from hashlib import sha1
import sys

ipad = b'123455678'
opad = b'abcdefghi'

def weak_hmac(m, k, ipad, opad):
    #XOR of they key and the ipad (we can only use ^ with integers)
    Si = int.from_bytes(ipad, sys.byteorder)^int.from_bytes(k, sys.byteorder)
    
    #Append the message to ther xored key (we had to guess that the message was also in bytes)
    s = (str(Si) + str(int.from_bytes(m, sys.byteorder))).encode()
    
    #Calculate the inner hash
    ihash = sha1(s).hexdigest()
    
    #XOR of the key and opad
    So = int.from_bytes(opad, sys.byteorder)^int.from_bytes(k, sys.byteorder)
    
    #Append the ihash to ther xored key
    s = (str(So) + str(ihash)).encode()
    
    #Calculate the outter hash / final HMAC
    md = sha1(s).hexdigest()
    
    return md
