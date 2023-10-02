from sys import *
import os
import hashlib
import logging as lg
lg.basicConfig(filename="log_11_3.txt",level=lg.DEBUG)

def Dup_Del_by_chksum(path):
    flg=os.path.isabs(path)
    if flg == False:
        path=os.path.abspath(path)
    exst=os.path.exists(path)

    if exst:
        c=1
        file_chk=dict()
        for fd,sbd,f1 in os.walk(path):
            for i in f1:
                abs=fd+"\\"+icn
                v1


