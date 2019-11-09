#!/bin/usr/env python3
# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib,os,threading,time

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

def checkIP():
    global out
    ipNow = os.popen('curl cip.cc').read()
    print(ipNow)
    ipNow = ipNow[ipNow.index('cc')+3:-1]
    if ipNow != out:
        out = ipNow
        msg = MIMEText(out, 'plain', 'utf-8')
        msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
        msg['To'] = _format_addr('管理员 <%s>' % to_addr)
        msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
        try:
            server = smtplib.SMTP(smtp_server, 25)
            server.set_debuglevel(1)
            server.login(from_addr, password)
        except Exception as ex:
            print(ex + '\nconnect smtp server failed.')
        try:
            server.sendmail(from_addr, [to_addr], msg.as_string())
        except Exception as ex:
            print(ex + '\n' + 'send failed\n')
        else:
            print('send succeed!')
        server.quit()

if __name__ == "__main__":
    out = '0.0.0.0'
    n = 1
    while True:
        print('This is the '+ str(n) + ' time to check ip.\n')
        checkIP()
        time.sleep(60)
        n += 1
