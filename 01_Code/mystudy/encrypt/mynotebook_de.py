#!/usr/bin/env python3


import os
import sys
import base64
import hashlib
import getpass


def init_authentication():
    u = getpass.getuser()
    if u.startswith('lim'):
        p = getpass.getpass(prompt="password: ")
        if len(p) < 1:
            sys.exit()
        m = hashlib.sha256()
        m.update(p.encode('utf-8'))
        if ('2f5b13d79c6868882ff3d3ab02f9d6519814f223dd306529c0d1000298dca309' != m.hexdigest()):
            sys.exit()
    else:
        sys.exit()


def myreverse(s):
    return s[::-1]


def cat_file():
    file = input('file: ')
    if os.path.isfile(file):
        with open(file, mode='r') as f:
            for line in f:
                s1 = base64.b64decode(bytes.fromhex(line.strip())).decode('utf-8')
                s = myreverse(s1)
                print(base64.b64decode(bytes.fromhex(s)).decode('utf-8'))


if __name__ == '__main__':
    init_authentication()
    cat_file()
