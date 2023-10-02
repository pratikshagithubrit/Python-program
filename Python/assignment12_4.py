import os
from sys import *
import psutil
import logging as lg
lg.basicConfig(filename="log_12_4.txt",level=lg.DEBUG)

def ProcessDisplay(dirname):
    os.makedirs(dirname)
    fpath=dir_name+"//"+"Running_process.txt"
    fobj=open(fpath,"w")
    fobj.writelines("Process_Name"+","+"P_id"+","+"Process_Username"+"\n")
    for pobj in psutil.Process_iter():
        pname=(pobj.name())
        pid=(pobj.pid)
        try:
            pun=(pobj.username())
        except Exception:
            pun="Access Denied"
        fobj.writelines(str(pname)+"."+str(pid)+"."+str(pun)+"\n")
    fobj.close()
    return fpath

def is_connected():
    try:
        import socket
        socket.createconnection(("www.google.com",80))
        return True

    except osError:
        pass

    return False

def sendemail(rp,emailid):
    if is_connected():
        import smtplib
        from email.mime.multipart import MIMEMultiple
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders
        sender="pratikshabpawar581@gmail.com"
        to=emailid
        data=MIMEMultiple()
        data['From']=sender
        data['To']=to
        data['subject']="this email send program about log report"

        import time
        localtime=time.astime(time.localtime(time.time()))
        body="this script generted on,"+localtime 
        data.attch(MIMEText(body,'plain'))
        filename="Process_log.txt"
        attachment=open(os.path.abspath(rp),"rb")
        p=MIMEBase('application','octet_stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header("content_Disposition","attachment;filename=%"%filename)
        data.attach(p)
        s=smtplib.SMTP('smtp.gmail.com',s87)
        s.starttls()
        s.login(sender,"enter ur password")
        text=data.as_string()
        s.sendmail(sender,to,text)
        s.quit()
    else:
        lg.info("no internet connection")

def main():
    if(len(argv)!=3):
        lg.info("give proper input.like process name(eg.notepad.exe)and email id(eg-marvellousinfosystem@gmail.com")
        exit()

    try:
        email=argv[2]
        rp=0
        import re
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        if(re.search(regex,email)):
            rp=ProcessDisplay(argv[1])
            if rp!=0:
                senderemail(rp,argv[2])
            else:
                lg.warning('not able to send email')
        else:
            lg.warning("give proper emailid")
            exit()
    except ValueError as e:
        lg.warning("invalid input",e)
    except Exception as e:
        lg.warning(e)

if __name__ == "__main__":
    main()