# Python 3 TLS encrypted reverse shell

A basic reverse shell writen in Python 3, all comms are using TLS.
consists of 2 scripts:

* reverse shell listener - listen for incoming connections and then allow the user to execute commands on the remote host
* reverse shell - connects back to the listener and allows remote command execution

## TLS cert and key
A certificate file and a key file are required for the TLS connection.
To generate the required files use openssl.
```
openssl req -x509 -newkey rsa:4096 -keyout serverkey.pem -out servercert.pem -days 365 -nodes
```
This creates a 1 year 4096 bit self signed certificate and key.

## Disclaimer
Do not use for illegal purposes. I do not accept any responsibility for any harm caused by using these scripts.

## Licence

MIT License

Copyright (c) 2021 Thomas W Whittam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
