#! phthon
# --*-- coding:utf-8 --*--


import os
import sys
import docx
import openpyxl
import re


def zhilian(filename):
    doc = docx.Document(filename)
    i = 0
    for para in doc.paragraphs:
        #re.search(, para.text)
        
        print("paragraphs[%d] ====>" % i)
        print(para.text)
        i += 1

    i = 0
    for tab in doc.tables:
        print("tables[%d]" % i)
        for row in range(tab.rows.__len__()):
            print("rows[%d]" % row)
            for j in range(tab.rows[row].cells.__len__()):
                print(tab.rows[row].cells[j].text)
        i += 1
        
        

def job51(filename):
    print("51job")
def liepin(filename):
    print("liepin")
def others(filename):
    print("others")


def resume_summary(filename):
    if not filename.endswith("docx"):
        print("%s is not a docx file." % filename)
        return

    if '猎聘' in os.path.basename(filename):
        liepin(filename)
    elif '51job' in os.path.basename(filename):
        job51(filename)
    elif '智联' in os.path.basename(filename):
        zhilian(filename)
    else:
        others(filename)
        


def walk_file(pathname):
    filelist = os.listdir(pathname)
    for filename in filelist:
        fullname = os.path.join(pathname, filename)
        if os.path.isdir(fullname):
            walk_file(fullname)
        elif os.path.isfile(fullname):
            #print(fullname)
            # job of specific
            resume_summary(fullname)
        else:
            print("%s is not normal file")


def main():
    if sys.version_info[0] != 3 :
        print("This program use python3, but your environment is python%d" % sys.version_info[0])
        sys.exit()

    # check input arguments for file path
    if len(sys.argv) != 2 :
        print("Please input a path of directory.")
        sys.exit()
    if not os.path.isdir(sys.argv[1]):
        print("You input %s is not a correct directory." % sys.argv[1])
        sys.exit()

    fullpath = sys.argv[1]

    # delete delimiter of tail
    while fullpath.endswith('\\') or fullpath.endswith('/'):
        fullpath = fullpath[:-1]

    # process job
    walk_file(fullpath)


if __name__ == "__main__":
    main()