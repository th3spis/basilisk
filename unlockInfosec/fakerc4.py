key=''.join([chr(v) for v in range(32)])

def encrypt(plaintext, k):
    return ''.join(chr(ord(k)^ord(t)) for k,t in zip(plaintext, k))

def get_prg(plaintext_size, k):
    # called separately
    n=len(k)
    k=list(k)
    keystream=''
    i=0
    j=0
    for _ in range(plaintext_size):
        i=(i+1)%n
        j=(j+ord(k[i]))%n
        t=k[i]
        k[i]=k[j]
        k[j]=t
        keystream+=k[(ord(k[i])+ord(k[j]))%n]
    return keystream
    pass # return keystream

def fake_rc4(plaintext, k):
    # called with plaintext and k'
    return encrypt(plaintext, k)
    pass # return ciphertext


plaintext='hello world'

print(fake_rc4(plaintext, get_prg(len(plaintext),key)))
