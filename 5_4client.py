import socket
import sys

if(len(sys.argv) >1):
   HOST = sys.argv[1]
else:
   print("\n\n Run like \n python3 5_4client.py 192.168.56.102 \n\n")
   exit(1)

b = socket.socket()

PORT = 5315

b.connect(('192.168.56.110', PORT))

print("Which file to be sent?")
Filename = input("Enter a filename:")
print("Filename: " + Filename)


File = open(Filename, "rb")
Data = File.read(1024)

while Data:
    print("\n\n-----Below message is received from server----- \n\n", b.recv(1024).decode("utf-8"))
    b.send(Data)
    Data = File.read(1024)


b.close()
