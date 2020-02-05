#!/usr/bin/env python3


import base64
import hashlib
import sys
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


def bytes2hex(bs):
    return ''.join(['%02x' % b for b in bs])


if __name__ == '__main__':
    init_authentication()

    s = input('>>')
    while len(s) > 0 and s[0] != 'q':
        bs = base64.b64encode(s.encode('utf-8'))
        h = bytes2hex(bs)
        r = myreverse(h)
        bs2 = base64.b64encode(r.encode('utf-8'))
        print(bytes2hex(bs2))

        s = input('>>')
