import random
import hashlib
import os
import math
from Crypto.Cipher import AES
from Crypto import Random

# you can use the imports, and you can solve with your own imports

p = 283
g = 47


class SecureChannel:

    def __init__(self, p, g):
        self.a = random.randint(1, p)

    def publish(self):
        #Diffie-Helman first step
        return (g**self.a)%p
        
    # Returns the IV prepended to the encrypted message. For simplicity's sake, the plaintext is always exactly 16 characters long
    def encrypt(self, gb, text):
        secreto = (gb**self.a)%p
        #converts the shared secret "secreto" into an encryption key for AES128 by casting it to a string of bytes, hashing it with SHA256, and using the first 16 bytes of the digest as the key
        k = hashlib.sha256(str(secreto).encode()).digest()[:16]
        #picks a random IV of 16 bytes
        iv = Random.get_random_bytes(16)
        #uses PyCrypto's AES128 in CBC mode to encrypt the text.
        cipher = AES.new(k, AES.MODE_CBC, iv)
        ciphertexto = cipher.encrypt(text) 
        return iv + ciphertexto
