import cv2
import zmq
import numpy as np
# We have imoprted cv2 for opening cam and showing images, zmq for communication to server and np for help in transformation

cap= cv2.VideoCapture(0)
#Initialized a variable for camera "0" indicated we'll be taking input from webcam
context= zmq.Context()
#Here we build the context for communication to server
socket = context.socket(zmq.REQ)
#From the context we create a request socket as we are client 
socket.connect("tcp://127.0.0.1:9999")
#For the example purpose we are taking port 9999 and localhost ip for sake of demonstration
#So far we have sent a connection req to server . As the server binds it we then can communicate


# THIS FUNCTION SENDS THE FRAME IMAGE TO THE ENDPOINT
def send_array(socket, A, flags=0, copy=True, track=False):
    md = dict(
        dtype = str(A.dtype),
        shape = A.shape,
    )
    # Made a dictionary of dtype of array and shape of array so that at server side we know
    # at the time of transforming array from  buffer we must know the shape to get it back.

    socket.send_json(md, flags|zmq.SNDMORE)
    #Sent the image using json to the server
    return socket.send(A, flags, copy=copy, track=track)
    # Finally sending the image in form of buffer to the server.

# THIS FUNCTION RECIEVIES THE ARRAY SENT FROM ANOTHER END
def recv_array(socket, flags=0, copy=True, track=False):
    md = socket.recv_json(flags=flags)
    # Recieves the json file containing dtype and shape of the required array
    msg = socket.recv(flags=flags, copy=copy, track=track)
    # msg is the buffer recived which contains the array
    A = np.frombuffer(msg, dtype=md["dtype"])
    # Using numpy and shape known  we transform the buffer into the array and reshape
    # it to required shape and then finally return it.
    return A.reshape(md['shape'])

# NOTE - If you wish to learn more about sending and receving arrays with zmq
#        then you can visit - https://pyzmq.readthedocs.io/en/latest/serialization.html

# The while True loop which continously send the frame images 
while True:
    _ , frame = cap.read()
    # Reading the frame images from the camera
    send_array(socket,frame)
    # Sent the frame to server for prediction and drawing boxes
    frame = recv_array(socket)
    # Recieved the frame with boxes drawn around face, eyes and lips
    cv2.imshow('Client side camera ', frame)
    # Show the frame to client

    k= cv2.waitKey(30) & 0xFF
    # Breaking the loop by pressing 'q' key to stop sending frames
    if k==ord('q'):
        break

cap.release()
# Release the webcam camers
cap.destroyallwindows()
# Destroys any window opened by the program.



#  -------------- Author Details ----------- 
#      Name - Anshuman Srivastava            
#      College- BIT Mesra, Ranchi             
#      Stream - IT                              
#      Session - 2018-2022                      
#                                                
#     Social Links to Contact            
    
#     [Github](https://github.com/anshumyname/)
#     [Linkedin](https://www.linkedin.com/in/anshuman-srivastava-84a0b3188/)
#     [Gmail](mailto:srivastavaanshuman33@gmail.com)    
#  -------------------------------------
    