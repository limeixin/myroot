#!/usr/bin/env python3


import sys
import hashlib
import getpass


if __name__ == '__main__':
    u = getpass.getuser()
    if u.startswith('lim'):
        p = getpass.getpass(prompt="password: ")
        if len(p) < 1:
            sys.exit()
        m = hashlib.sha256()
        m.update(p.encode('utf-8'))
        if ('2f5b13d79c6868882ff3d3ab02f9d6519814f223dd306529c0d1000298dca309' != m.hexdigest()):
            sys.exit()

        k = getpass.getpass(prompt="key: ")
        n = input('fn: ')
        h = hashlib.blake2b(digest_size=16, key=k.encode('utf-8'))
        h.update(n.encode('utf-8'))
        print(h.hexdigest())
    else:
        sys.exit()
