# coding:utf8
# created at 2018/6/19.

import os
import sys

checkdir = sys.argv[1]
kword = sys.argv[2]

def checkword(fs,kword):
    f = open(fs,'r')
    if kword == 'sleep':
        if "sleep" in f.read():
            print("%s 该文件包含sleep" % fs)
            exit(1)
        else:
            return
    elif kword == 'declare':
        if 'declare' in f.read():
            return
        else:
            print("%s 该文件未包含declare" % fs)
            exit(1)
    else:
        pass

if os.path.isdir(checkdir):
    for root,dirs,files in os.walk(checkdir):
        for i in files:
            fs = os.path.join(root,i)
            if kword == "sleep":
                if "jax" in fs:
                    continue
                else:
                    if fs.endswith(".php"):
                        checkword(fs,kword)
            elif kword == "declare":
                if fs.endswith(".php"):
                    checkword(fs,kword)
            else:
                pass
    print("语法检测通过")
else:
    print("传入参数必须是目录")
