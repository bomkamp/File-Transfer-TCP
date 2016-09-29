@AUTHOR: Greg Bomkamp
@DATE: 9/28/2016

run the program by:

	1. Starting 'python3 ftps.py <port number>' command on your server terminal replacing <port number> with a number from 1-65535.
	
	2. Starting 'python3 ftpc.py <remote-IP-on-gamma> <remote-port-on-gamma> <local-file-to-transfer>' on your client terminal replacing <remote-IP-on-gamma> with the server's IP or domain name, <remote-port-on-gamma> with the port used in step 1, and <local-file-to-transfer> with a file you would like to be transfered to the server.
	
	3. The program will run and copy the file over a TCP connection into a subdirectory: 'recv' in the current directory that the server is in.

Any requirements will notify the user upon bad inputs.
