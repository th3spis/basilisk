import sys
sys.path.insert(0,'.') 
from Root.fetch import fetch
import time
import os

def did_fetch(user, url):
    os.environ['USER'] = user 
    t1 = time.time()
    fetch(url)
    t2 = time.time()
    diferencio = t2-t1
    return diferencio < 0.1
