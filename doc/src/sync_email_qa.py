#!/usr/bin/python3
# -*- coding: UTF-8 -*-
""" 
# Sync email qa context
# Matianer: Thomas
# Update: 2021-10-11
# License: MIT
# Version：0.1
"""

import os 
import smtplib
from email.message import EmailMessage
from email.header import decode_header
from email.utils import parseaddr
import poplib
from email.parser import Parser

user = 'haiyuan.bian@apulis.com'
password = 'Aiperf@2025'
smtpsrv = "partner.outlook.cn"
pop3_server = 'partner.outlook.cn'
msg = EmailMessage()
msg['Subject'] = 'Email Testing with Python'
msg['From'] = 'xxxxxxxxx@xxxxxxxxx.com'
msg['To'] = 'xxxxxxxx@163.com'

message = {}

def smtp_client():
    smtpserver = smtplib.SMTP(smtpsrv,587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(user, password)
    return smtpserver

def close_session(session):
    session.close()

def send_msg(session, args):
    session.send_message (msg)

def get_msg(session):
    session.close()

def select_msg(session):
    session.close()


# input email address, password and pop3 server domain or ip address

def pop3_connect(pop3_server):
    # connect to pop3 server:
    server = poplib.POP3_SSL(pop3_server)
    # print out the pop3 server welcome message.
    print(server.getwelcome().decode('utf-8'))

    # user account authentication
    server.user(user)
    server.pass_(password)
    # stat() function return email count and occupied disk size
    print('Messages: %s. Size: %s' % server.stat())
    # list() function return all email list
    resp, mails, octets = server.list()
    # print(mails)
    return server, mails

def get_mails(server, mails):
    # retrieve the newest email index number
    index = len(mails)
    # server.retr function can get the contents of the email with index variable value index number.
    resp, lines, octets = server.retr(index)

    # lines stores each line of the original text of the message
    # so that you can get the original text of the entire message use the join function and lines variable. 
    # msg_content = b'\r\n'.join(lines).decode('utf-8')
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # now parse out the email object.
    msg = Parser().parsestr(msg_content)
    return msg

# indent用于缩进显示:
def parse_msg(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
                    message["header"] = {"hdr":hdr,"addr":addr,"name":name,} 
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            parse_msg(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset
    
def decode_str(strings):
    value, charset = decode_header(strings)[0]
    if charset:
        value = value.decode(charset)
    return value


def close_server(server):
    # close pop3 server connection.
    server.quit()


# # get email from, to, subject attribute value.
# email_from = decode_header(msg.get('From'))
# email_subject = msg.get('Subject')
# print('Subject {} From {} '.format(email_subject, email_from))

'''
参考链接;
https://docs.microsoft.com/zh-cn/Exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365?redirectSourcePath=%252fen-us%252farticle%252fHow-to-set-up-a-multifunction-device-or-application-to-send-email-using-Office-365-69f58e99-c550-4274-ad18-c805d654b4c4
https://pythoncircle.com/post/36/how-to-send-email-from-python-and-django-using-office-365/
https://medium.com/@neonforge/how-to-send-emails-with-attachments-with-python-by-using-microsoft-outlook-or-office365-smtp-b20405c9e63a
'''


if __name__== "__main__":
    message = {}
    server, mails = pop3_connect(pop3_server)
    msg = get_mails(server, mails)
    message = parse_msg(msg)
    print("============={}".format(message))