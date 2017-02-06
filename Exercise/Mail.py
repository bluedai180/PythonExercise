import imaplib
import poplib
import email
import email.header
import email.utils
from email.parser import Parser

example_pop3_server = "pop3.163.com"
example_user = ""
example_password = ""

pop3_server = 'pop.263.net'
user = ''
password = ''

server = poplib.POP3_SSL(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome())
server.user(user)
server.pass_(password)
mailfrom = []

print('Messages: %s. Size: %s' % server.stat())

resp, mails, octets = server.list()
print(mails)
# index = len(mails)
# resp, lines, octets = server.retr(index)
# msg_content = '\r\n'.join(lines)
# msg = Parser().parsestr(msg_content)
# server.quit()

# mail = imaplib.IMAP4_SSL('imap.263.net', 993)
# mail.login(user, password)
# mail.list()
# mail.select()
# typ,data=mail.search(None, 'UNSEEN')
# print(data)