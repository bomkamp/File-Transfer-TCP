#!/usr/bin/env python3

#Author: Greg Bomkamp: section 11:10 - 12:30 Tu Th

import sys,os
from socket import *

#check for correct argument amount.
if(len(sys.argv)!=2):
	print('You must supply exactly one argument: local port number')
	sys.exit()

#check that the given argument is valid
try:	
	if not (int(sys.argv[1]) in range(1,65535)):
		print('Your port number must an integer within 1 and 65535.')
		sys.exit()
except:
	print('Your port number must an integer within 1 and 65535.')
	sys.exit()
	
serverPort = int(sys.argv[1])

#create welcoming socket
serverSocket = socket(AF_INET,SOCK_STREAM)

#try to bind serverPort, except throws an error if any problems are encountered.
try: 
	serverSocket.bind(('',serverPort))
except:
	print('There was a problem binding a socket to your port.')
	sys.exit()

#ready to listen for transfer
serverSocket.listen(1)
print('Server successfully initialized and ready to receive.')

#Accept a ready connection
connectionSocket, addr = serverSocket.accept()

#Grab necessary inital information from first 24 bytes.
numBytes = connectionSocket.recv(4)
numBytes = int.from_bytes(numBytes,byteorder='big')
fileName = connectionSocket.recv(20)
fileName = fileName.decode('ASCII').strip()

#Setup new file location and create initial file to copy to. (This is taken from copy.py from lab 1)
subDir = os.path.join(os.getcwd(),'recv') #create the path for the new subdirectory
pathToNewFile = os.path.join(subDir,str(fileName)) #get the path for the new file

if not (os.path.exists(subDir)):
	try:
		os.makedirs(subDir) #create directory only if it doesnt already exist.
	except:
		print('There was a problem creating the directory for the new file. Terminating program.')
		
#open new file to copy to
try:
	newCopy = open(pathToNewFile,'wb')
except:
	print('There was a problem writing a new file to '+ pathToNewFile)

#start tranferring file contents 500 bytes at a time.
while numBytes > 500:
	partialFile = connectionSocket.recv(500)
	newCopy.write(partialFile)
	numBytes-=500;
	
#Final transfer when less than 500 bytes are left
if numBytes > 0:
	partialFile = connectionSocket.recv(numBytes)
	newCopy.write(partialFile)

print('File transfer complete. File is located at: '+ pathToNewFile)
#Finish transfer and close all that is left open.
newCopy.close()
connectionSocket.close()
serverSocket.close()
