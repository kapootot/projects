#!/usr/bin/python

import socket


def main():
    s = socket.socket()
    host = '127.0.0.1'
    port = 5000
    s.bind((host, port))
    s.listen(1)
    c, addr = s.accept()
    client_addr = c.recv(512)
    print("Accepted connection from client.")
    while True:
        print('Waiting for data from: ' + str(client_addr))
        data = c.recv(1024)
        if not (data):
            break
        c.send('This is your data...:\n')
        c.send(str(data))
        c.send("\nBUT - this is your DATA:\n")
        c.send(str(data.upper()))
        c.send("\nThanks!")
    c.close()


main()
