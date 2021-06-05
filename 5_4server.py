import socket

b = socket.socket()

HOST = "192.168.56.110"
PORT = 5315

print('Server is now listening to :', PORT)

b.bind(('192.168.56.110', PORT))

b.listen(10)

File = open("test.txt", "wb")
print('\n test.txt will be copied at server \n')

while True:
	conn, addr = b.accept()

	message = "\n\n Hey Client[IP address: " + addr[0] + "], \n---Hello! Welcome to Server--- \n\n"
	conn.send(message.encode())

	recvdata = conn.recv(1024)
	while recvdata:
		File.write(recvdata)
		recvdata = conn.recv(1024)

	File.close()
	print('\n File copied succeed \n')

	conn.close()
	print('\n Connection closed by server \n')


	break
