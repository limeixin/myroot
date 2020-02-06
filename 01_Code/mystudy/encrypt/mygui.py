#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sys
import base64
import hashlib
import getpass

import tkinter as tk
import tkinter.messagebox


def tanslate_filename():
    fn = name_e.get()
    

def readf():
    fname = file.get()
    t.insert('insert', fname)


def savef():
    ok = tk.messagebox.askokcancel('提示', '真的需要保存吗？')
    if not ok:
        return
    t.insert('insert', "保存")


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