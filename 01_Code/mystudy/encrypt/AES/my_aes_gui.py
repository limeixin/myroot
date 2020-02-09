#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sys
import base64
import hashlib
import getpass

import tkinter as tk
import tkinter.messagebox

from Crypto.Cipher import AES


filename_key = ''
file_key = '1234567890123456'


###############################################################################
## AES
###############################################################################
# """
# AES加密解密工具类
# 数据块128位
# key 为16位
# iv 为16位，且与key相等
# 字符集utf-8
# 输出为base64
# AES加密模式 为cbc
# 填充 pkcs7padding
# """

def pkcs7padding(text):
    """
    明文使用PKCS7填充
    最终调用AES加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理
    :param text: 待加密内容(明文)
    :return:
    """
    bs = AES.block_size  # 16
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    # tips：utf-8编码时，英文占1个byte，而中文占3个byte
    padding_size = length if(bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
    padding_text = chr(padding) * padding
    return text + padding_text


def pkcs7unpadding(text):
    """
    处理使用PKCS7填充过的数据
    :param text: 解密后的字符串
    :return:
    """
    length = len(text)
    unpadding = ord(text[length-1])
    return text[0:length-unpadding]


def encrypt(key, content):
    """
    AES加密
    key,iv使用同一个
    模式cbc
    填充pkcs7
    :param key: 密钥
    :param content: 加密内容
    :return:
    """
    key_bytes = bytes(key, encoding='utf-8')
    iv = key_bytes
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    # 处理明文
    content_padding = pkcs7padding(content)
    # 加密
    encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
    # 重新编码
    result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
    return result


def decrypt(key, content):
    """
    AES解密
     key,iv使用同一个
    模式cbc
    去填充pkcs7
    :param key:
    :param content:
    :return:
    """
    key_bytes = bytes(key, encoding='utf-8')
    iv = key_bytes
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    # base64解码
    encrypt_bytes = base64.b64decode(content)
    # 解密
    decrypt_bytes = cipher.decrypt(encrypt_bytes)
    # 重新编码
    result = str(decrypt_bytes, encoding='utf-8')
    # 去除填充内容
    result = pkcs7unpadding(result)
    return result
###end AES=====================================================================


def init_file_key():
    """
    使用16字节长度的密码
    """
    key_len = len(filename_key)
    if key_len > 16:
        file_key = filename_key[0:16]
    elif key_len == 16:
        file_key = filename_key
    else:
        padlen = 16 - key_len
        file_key = filename_key + 'goodgoodstudydaydayup'[0:padlen]


def myreverse(s):
    return s[::-1]


def bytes2hex(bs):
    return ''.join(['%02x' % b for b in bs])


def tanslate_filename():
    fn = name_e.get()
    if len(fn) < 1:
        return
    # encrypt filename
    h = hashlib.blake2b(digest_size=16, key=filename_key.encode('utf-8'))
    h.update(fn.encode('utf-8'))

    #clear Entry, and write encode filename
    name_e.delete(0, tk.END)
    name_e.insert(0, h.hexdigest())


# def encode_text(s):
    # bs = base64.b64encode(s.encode('utf-8'))
    # h = bytes2hex(bs)
    # r = myreverse(h)
    # bs2 = base64.b64encode(r.encode('utf-8'))
    # return bytes2hex(bs2)


# def decode_text(line):
    # s1 = base64.b64decode(bytes.fromhex(line.strip())).decode('utf-8')
    # s = myreverse(s1)
    # return base64.b64decode(bytes.fromhex(s)).decode('utf-8')


###############################################################################
## read file and show it in tk.text
###############################################################################
def readf():
    t.delete('0.0', tk.END)
    fname = file.get()
    if len(fname) < 1:
        return
    if not os.path.isfile(fname):
        tk.messagebox.showerror('错误', '访问的文件不存在')
        return

    try:
        f = open(fname)
        txt = f.read()
        t.insert('end', decrypt(file_key, txt))

    except OSError as reason:
        tk.messagebox.showerror('错误', '访问的文件不存在' + str(reason))
    except TypeError as reason:
        tk.messagebox.showerror('错误', '数据类型错误' + str(reason))
    except:
        tk.messagebox.showerror("异常错误", sys.exc_info()[0])

    finally:  #finally语句，无论有没有报错，都会被执行到
        f.close()


###############################################################################
## save file 
###############################################################################
def savef():
    is_save_success = False

    fname = file.get()
    if len(fname) < 1:
        return

    file_bak_name = fname + '.bak'

    # Text get, '0.0' is from row 0 and column 0
    file_text = t.get('0.0', 'end')

    ok = tk.messagebox.askokcancel('提示', '真的需要保存吗？')
    if not ok:
        return
    #t.insert('insert', "保存")

    try:
        f = open(file_bak_name, 'w')
        en_file_text = encrypt(file_key, file_text)
        en_file_text_len = len(en_file_text)
        write_len = f.write(en_file_text)
        if write_len == en_file_text_len:
            # mark save success
            is_save_success = True
        else:
            tk.messagebox.showerror('错误', '保存未完成 ' + str(write_len) + ' != ' + str(en_file_text_len))

    except OSError as reason:
        tk.messagebox.showerror('错误', '写文件错误' + str(reason))
        if os.path.isfile(file_bak_name):
            os.remove(file_bak_name)
    except TypeError as reason:
        tk.messagebox.showerror('错误', '数据类型错误' + str(reason))
        if os.path.isfile(file_bak_name):
            os.remove(file_bak_name)
    except:
        tk.messagebox.showerror("异常错误", sys.exc_info()[0])

    finally:  #finally语句，无论有没有报错，都会被执行到
        f.close()
        if  is_save_success:
            # remove old file
            if os.path.isfile(fname):
                os.remove(fname)
            #rename .bak file to file
            os.rename(file_bak_name, fname)



###############################################################################
## authentication
###############################################################################
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


###############################################################################
## get filename key from user keyboard input
###############################################################################
def init_filename_encrypt_key():
    k = getpass.getpass(prompt="filename key: ")
    if len(k) < 1:
        sys.exit()

    # global filename_key 
    filename_key = k



###############################################################################
## main
###############################################################################
if __name__ == '__main__':
    init_authentication()
    init_filename_encrypt_key()
    init_file_key()

    ###############################################################################
    ## GUI
    ###############################################################################
    top = tk.Tk()
    top.title("个人文本")

    frm1 = tk.Frame(top)
    frm1.pack(side='top', fill=tk.X)

    name_e = tk.Entry(frm1)
    name_e.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
    b1 = tk.Button(frm1, text="转文件名", command=tanslate_filename)
    b1.pack()


    frm2 = tk.Frame(top)
    frm2.pack(fill=tk.X)

    save = tk.Button(frm2, text="保存", command=savef)
    save.pack(side=tk.RIGHT)
    openf = tk.Button(frm2, text=" 读取文件 ", command=readf)
    openf.pack(side=tk.RIGHT)
    file = tk.Entry(frm2)
    file.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)


    frm3 = tk.Frame(top)
    frm3.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)

    scroll_y = tk.Scrollbar(frm3)
    scroll_y.pack(side=tk.RIGHT,fill=tk.Y)

    t = tk.Text(frm3)
    t.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)

    scroll_y.config(command=t.yview)
    t.config(yscrollcommand=scroll_y.set)

    top.mainloop()