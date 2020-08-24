alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)

def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)
    
def brute_force(ciphertext):
    return "".join([decrypt(ciphertext, k) + '\0 ' + str(k) + '\n' for k in range(1,25)])

#bruteforce this given text, by printing all possibilites and the used key
print(brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe"))
