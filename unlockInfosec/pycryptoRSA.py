from Crypto.PublicKey import RSA
#https://pythonhosted.org/pycrypto/Crypto.PublicKey.RSA._RSAobj-class.html


key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def encrypt(m, public_key):
    pu_key = RSA.importKey(public_key)
    return pu_key.encrypt(str(m).encode(),0)


def decrypt(c, private_key):
    pr_key = RSA.importKey(private_key)
    return pr_key.decrypt(c)
