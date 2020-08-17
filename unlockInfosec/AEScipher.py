#! /usr/bin/python3 
from Crypto.Cipher import AES
from Crypto import Random


def aes_encrypt(plaintext, k):
    # return iv + ciphertext (in bytes)
    iv = Random.get_random_bytes(16)
    #Crypto.Cipher.AES.new(key, mode, *args, **kwargs)
    cipher = AES.new(k, AES.MODE_CBC, iv)
    ciphertexto = cipher.encrypt(plaintext) 
    print(ciphertexto)
    print(iv)
    print((iv + ciphertexto)[16:])
    return iv + ciphertexto

def aes_decrypt(ciphertext, k):
    pass # return plaintext (in 'latin1')
    cipher = AES.new(k, AES.MODE_CBC, ciphertext[0:16])
    plaintext = cipher.decrypt(ciphertext[16:])
    return plaintext.decode()
    
print(aes_decrypt(aes_encrypt('helicoptero cool','absgahasahstdhsy'), 'absgahasahstdhsy'))
