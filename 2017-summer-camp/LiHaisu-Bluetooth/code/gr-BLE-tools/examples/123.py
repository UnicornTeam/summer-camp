import zmq  

context = zmq.Context()  
socket = context.socket(zmq.SUB)  
socket.connect("tcp://127.0.0.1:23333")  
socket.setsockopt(zmq.SUBSCRIBE,'')
while 1:
	print socket.recv()[10:]	

