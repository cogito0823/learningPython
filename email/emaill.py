#!/usr/bin/env python3
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

def send(out):
    msg = MIMEText(out, 'plain', 'utf-8')
    msg['From'] = _format_addr('Raspberry Pi <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('现行IP', 'utf-8').encode()
    try:
        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
    except Exception as ex:
        print('\nconnect smtp server failed.Check up exit.Please check you smtp server\'s setting.\n')
        return
    try:
        server.sendmail(from_addr, [to_addr], msg.as_string())
    except Exception as ex:
        print('\n' + 'send failed.Check up exit.\n')
        return
    server.quit()
    print('\nsend succeed!\n')

def check_up():
    global out
    ipNow = checkIp()
    if ipNow:
        if ipNow != out:
            print('The IP address has been changed to '+ ipNow + '\n\nStarting to send email...\n')
            out = ipNow
            send(out)
        else:
            print('The IP address has not been changed.\n')
    print('Waiting for the next time to check up.\n\n-------------------------------------------------------\n')

def checkIp():
    ipNowAll = os.popen('curl cip.cc').read()
    print(ipNowAll)
    try:
        ipNow = ipNowAll[ipNowAll.index('cc')+3:-1]
    except ValueError:
        print('Can\'t connect to net. Check up exit.')
        return False
    return ipNow
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
        check_up()
        time.sleep(6)
        n = n + 1
