#!/usr/bin/env python3


import sys
import hashlib



if __name__ == '__main__':
    str = sys.argv[1]

    #md5
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    print(m.hexdigest())

    #sha
    m = hashlib.sha256()
    m.update(str.encode('utf-8'))
    print(m.hexdigest())

    #blake2b
    #digest_size must >= 16
    h = hashlib.blake2b(digest_size=32, key=b'mypassword1')
    h.update(str.encode('utf-8'))
    print(h.hexdigest())

    
    