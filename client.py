import socket
def send(msg):
	s.send(msg.encode())
def makeConnection():
	try: 
		s.connect((host,port))
	except:
		print("Please enter valid address")
def receive():
	msg = s.recv(1024)
	while msg:
		print("Received: ",msg.decode())
		msg = recv(1024)
def conversations():
	while True:
		message = input("Enter something: ")
		if message == "exit()":
			break
		send(message)
host = input("Enter address: ")
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
makeConnection()
'''while msg:
	print("Received: ",msg.decode())
	msg = s.recv(1024)'''
conversations()
s.close()
