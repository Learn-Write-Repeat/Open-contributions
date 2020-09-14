import zmq
from time import sleep

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:9999")

while (True):
    message = socket.recv()
    print(f"Received request: {message}")
    sleep(1)
    socket.send(b"Message Received")
    if message == b'stop':
        break

    socket.send(b"stop")
	socket.recv()