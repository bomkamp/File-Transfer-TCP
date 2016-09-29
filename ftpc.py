#!/usr/bin/env python3

#Author: Greg Bomkamp: section 11:10 - 12:30 Tu Th+

import sys,os
from socket import *

#First check to be sure that exactly three arguments were supplied: remote IP, remote Port, and file to transfer.
if(len(sys.argv)!=4):
	print('You must suppliy exactly three arguments: remote IP/server name, remote Port, and file to transfer.')
	sys.exit()
	
ipAdd = sys.argv[1] #get IP
portNum = int(sys.argv[2]) #get Port
fileName = str(sys.argv[3]) #get file name 

#open the file to copy
try:
	oldFile = open(fileName,'rb')
except:
	print('There was a problem opening the file to copy.')
	sys.exit()
	
	
#setup network connection	
try:
	clientSocket = socket(AF_INET,SOCK_STREAM)
	clientSocket.connect((ipAdd,portNum))
except:
	print('There was a problem establishing the connection, is the server ready to receive?')
	sys.exit()

#send file size
fileSize = os.path.getsize(fileName).to_bytes(4,byteorder='big')
clientSocket.send(fileSize)

#send file name
fileName = fileName.rjust(20)
clientSocket.send(fileName.encode('ASCII'))

#loop and send file in 500 byte increments
try:
	readBytes = oldFile.read(500)
	while (readBytes):
		clientSocket.send(readBytes)
		readBytes = oldFile.read(500)
except:
	print('There was an error sending part of the file to '+ ipAdd)

print('File successfully transferred.')
#close all connections
oldFile.close()
clientSocket.close()
