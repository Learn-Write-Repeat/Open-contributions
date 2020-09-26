import cv2
import zmq
import numpy as np

cap= cv2.VideoCapture(0)
context= zmq.Context()
print("Connecting to context")
socket = context.socket(zmq.REQ)
# socket.setsockopt(zmq.SUBSCRIBE, b"")
socket.connect("tcp://127.0.0.1:9999")
print("Socket created")

def send_array(socket, A, flags=0, copy=True, track=False):
    """send a numpy array with metadata"""
    md = dict(
        dtype = str(A.dtype),
        shape = A.shape,
    )
    socket.send_json(md, flags|zmq.SNDMORE)
    return socket.send(A, flags, copy=copy, track=track)

def recv_array(socket, flags=0, copy=True, track=False):
    """recv a numpy array"""
    md = socket.recv_json(flags=flags)
    msg = socket.recv(flags=flags, copy=copy, track=track)
    A = np.frombuffer(msg, dtype=md["dtype"])
    return A.reshape(md['shape'])

# li = np.array([[4,23,25],[235,65,23]],dtype=np.int32)
# send_array(socket, li )

while True:
    _ , frame = cap.read()
    # _, frame = image_hub.send_image(rpi_name, frame)
    # _ , image= image_hub.recv_image()
 
    send_array(socket,frame)
    print("Sended frame")
    frame = recv_array(socket)
    print("Recived frame")
    cv2.imshow('Client side camera ', frame)

    k= cv2.waitKey(30) & 0xFF
    if k==ord('q'):
        break

cap.release()
cap.destroyallwindows()

    