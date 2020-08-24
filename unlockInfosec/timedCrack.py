import time
import sys 
from Root.pswd import real_password

def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def crack_password():
    v1 = '0'
    v2 = '0'
    v3 = '0'
    v4 = '0'
    cracked = False
    while not cracked:
        t1 = time.time()
        cracked = check_password(v1+v2+v3+v4)
        t2 = time.time()
        dif = t2-t1
        #print(dif)
        if(dif < 0.2):
            v1 = str(int(v1) + 1)
        elif (dif < 0.3):
            v2 = str(int(v2) + 1)
        elif (dif < 0.4):
            v3 = str(int(v3) + 1)
        elif(not cracked):
            v4 = str(int(v4) + 1)
    print('Cracked! Code: ' + v1+v2+v3+v4)
            
            
crack_password()
