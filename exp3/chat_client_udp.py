import socket
udp_port=('172.16.5.254',2223)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(udp_port)
while True:
	print "client:"
	input=raw_input()
	if input=="bye" or input=="exit":
		s.sendto(input,('172.16.2.227',2223))
		s.close()
	else:
		s.sendto(input,('172.16.2.227',2223))
	#print "hi"
	data,address=s.recvfrom(1024)
	#print "hi"
	print "server:"+str(data)
