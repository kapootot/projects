#!/usr/bin/python

import socket

def main():
	
	s = socket.socket()
	print 'Client Socket created!'
	host = '127.0.0.1'
	port = 5000
	s.connect((host, port))
	s.send(socket.gethostname())
	print 'Connected to server'
	data = raw_input('Enter Data to be sent to server:')
	
	while data != 'q':
		s.send(data)
 		print s.recv(1024)
		data = raw_input('Enter Data to be sent to server:')	
	s.close()	
main()
	
