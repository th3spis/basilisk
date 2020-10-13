import hashlib

def sign(line):
    x = hashlib.sha1()
    x.update(line)
    #since sha1 returns a hash of 20 letters i decided just to cut it
    return x.hexdigest()[:20]

def scan(paths, signature):
    alert = []  #clear list for the bad files
    for path in paths: #iterate through each path
        with open(path) as file:  #using "with open" statement there is no need to close files
            for line in file: #iterate through the lines
                line = line.rstrip('\n') # drop the \n in the end of the lines
                line = line.encode('utf-8') #needed for the hash computation
                if sign(line) == signature: #compare the line signiture to the given one
                    alert.append(path) #add the file name to the bad files list
                    continue #since we already found out it`s a bad file skip to next path
    return alert
