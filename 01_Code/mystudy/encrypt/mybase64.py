#!/usr/bin/env python3


import base64
import sys


#
# translate bytes string to hex string
#
def bytes2hex(bs):
    return ''.join(['%02x' % b for b in bs])


#
# translate hex string to bytes string
#
def hex2bytes(hs):
    return bytes.fromhex(hs)


#
# translate bytes string to utf-8 char string
##
def bytes2str(bs):
    return bs.decode('utf-8')


#
# translate string to utf-8 bytes
#
def str2bytes(str):
    return str.encode('utf-8')


if __name__ == '__main__':
    bs = str2bytes(sys.argv[1])
    b64 = base64.b64encode(bs)

    #output hex string
    hstr = bytes2hex(b64)
    print("hex: " + hstr)

    bstr = bytes2str(b64)
    print("str: " + bstr)

    #translate for decode
    newbytes = hex2bytes(hstr)
    newb64decode = base64.b64decode(newbytes)

    #output base64 decode string
    newarg = bytes2str(newb64decode)
    print("you inpurt arg1 is: " + newarg)


