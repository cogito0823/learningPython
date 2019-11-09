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
    ipNowAll = os.popen('curl cip.cc').read()
    try:
        ipNow = ipNowAll[ipNowAll.index('cc')+3:-1]
    except ValueError as ee:
        print('\nCan\'t connect to net. Check up exit.\n\nWaiting for next time to check...\n')
        return
    if ipNow != out:
        print(ipNowAll)
        print('The IP address has been changed to '+ ipNow + '\n\nStarting to send email...\n')
        out = ipNow
        msg = MIMEText(out, 'plain', 'utf-8')
        msg['From'] = _format_addr('Raspberry Pi <%s>' % from_addr)
        msg['To'] = _format_addr('管理员 <%s>' % to_addr)
        msg['Subject'] = Header('现行IP', 'utf-8').encode()
        try:
            server = smtplib.SMTP(smtp_server, 25)
            server.set_debuglevel(1)
            server.login(from_addr, password)
        except Exception as ex:
            print('\nconnect smtp server failed.Check up exit.Please check you smtp server\'s setting.\n\nWaiting for the next time to check.\n')
            return
        try:
            server.sendmail(from_addr, [to_addr], msg.as_string())
        except Exception as ex:
            print('\n' + 'send failed.Check up exit.\n\nWaiting for the next time to check.\n')
            return
        server.quit()
        print('\nsending succeed!\n\nWaiting for the next time to check...\n')
    else:
        print('\nThe IP address has not been changed.\n\nWaiting for the next time to check...\n')
    return

if __name__ == "__main__":
    out = '0.0.0.0'
    n = 1
    time_start = time.time()
    while True:
        time_now = time.time()
        m, s = divmod(time_now-time_start, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        print('\nThis script has been running for ' + '%d days %02d hours %02d minutes %02d seconds.\n' % (d,h,m,s) +  '\n' 'It is the', n, 'times to check up.\n')
        checkIP()
        time.sleep(6)
        n += 1
