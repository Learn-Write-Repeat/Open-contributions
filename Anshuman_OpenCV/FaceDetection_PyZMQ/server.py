import dlib, cv2
import socket , zmq
import numpy as np


getface = dlib.get_frontal_face_detector()
getlandmark= dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")
# sender = imagezmq.ImageSender(connect_to="tcp://jeff-macbook:5555")
# rpi_name = socket.gethostname()

context= zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:9999")
print("Connect and socketed")

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


# fr = recv_array(socket)
# print(fr)
while True:

    # _,frame= cap.read()
    frame = recv_array(socket)
    print(type(frame),frame.shape)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces= getface(gray)

    for face in faces:
        x, y= face.left(), face.top()
        w, h= face.right()-x, face.bottom()-y
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(0,0,255),3)
        landmars = getlandmark(gray, face)
        hx= landmars.part(48).x-10
        hy= landmars.part(51).y-10
        ww= landmars.part(54).x-landmars.part(48).x+10
        hh = landmars.part(57).y- landmars.part(51).y+10

        frame= cv2.rectangle(frame, (hx,hy),(hx+ww,hy+hh),(0,255,0),3)

        hx= (landmars.part(37).x+landmars.part(40).x)/2
        hy= (landmars.part(37).y+landmars.part(40).y)/2
        ww= (landmars.part(39).x-landmars.part(36).x+10)/2
        # hh = landmars.part(38).y- landmars.part(41).y+50

        frame= cv2.circle(frame, (hx,hy),ww,(0,255,255),3)

        hx= (landmars.part(43).x+landmars.part(46).x)/2
        hy= (landmars.part(43).y+landmars.part(46).y)/2
        ww= (landmars.part(45).x-landmars.part(42).x+10)/2
        # hh = landmars.part(44).y- landmars.part(47).y+50

        frame= cv2.circle(frame, (hx,hy),ww,(0,255,255),3)

    # plain = np.ravel(frame)
    # sh = frame.shape
    send_array(socket,frame)

#     # cv2.imshow('Face',frame)
    k= cv2.waitKey(30) & 0xFF
    if k==ord('q'):
        break





