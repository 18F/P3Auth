# This file is responsible for checking secure hashes
# against configured user/password sistuations.
import random, string


import os
import pickle
import hashlib
P3APISALT = "changeme"
RelativePathToPasswordFile = '../configuration/p3api.passwords.txt'
RelativePathToHashesFile = '../configuration/p3api.hashes.txt'

def generatePasswords():
    hsh_file = RelativePathToHashesFile
    pwd_file = RelativePathToPasswordFile
    pwds = {}
    hshs = {}
    for i in range(500):
        # Add password
        username = "changeme"+str(i)
        # Warning!  This is temporary!  We really want to
        # create random creds instead, but we need to
        # know the creds to mail them out to people,
        # So this is just a test.

        length = 25 # change this to something reasonable
        chars = string.ascii_letters + string.digits

        password = ''.join(random.choice(chars) for i in range(length))

        pwds[username] = password
        hshs[username] = hashlib.sha256(password+P3APISALT).hexdigest()

    # Save to disk
    with open(hsh_file, "wb") as hf:
        pickle.dump(hshs, hf)
    with open(pwd_file, "wb") as pf:
        pickle.dump(pwds, pf)

# invoke the function.
generatePasswords()
