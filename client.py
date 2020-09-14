import zmq

context = zmq.Context()
print("Connecting to Server on port 9999")
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:9999")
print('Sending Hello')
socket.send(b"Hello")
print('Waiting for answer')
message = socket.recv()
print(f"Received: {message}")
