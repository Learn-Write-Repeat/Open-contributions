# Face,Eye and Lip Detection & PyZMQ

So in this section we'll learn not only about how we can perform face,eye and lip detection but also how we will be transferring frames of camera from client side to server , then detection will be done on server side. Finally then the predictions  will be displayed back to client side.

Let's get familiar with PyZMQ first

## PyZMQ
PyZMQ is a python version of ZeroMQ which again is a library which is used to set up messaging and communication between applications and processes quick and asynchronously.<br>
<img src="https://www.rastertek.com/pic0181.gif" align="right" style="padding:10px;" >
Although there are other methods available for file transfer in client server models ZMQ one of the greatest advantage of ZMQ is that it can be used for message queuing without a message borker.<br>
If you wish to learn more about ZMQ and client server architechture ,then  you can refer [here](https://github.com/Learn-Write-Repeat/Open-contributions/blob/master/Akshay_Python_PyZMQ.md).

<br><br>
Now we have a little knowledge of ZMQ so we'll proceed with our next topic 68 Landmarks of Face which will be useful for our eye and lip detection.

## 68 Landmarks of Face
As you can see in the image we have total 68 
<img src="https://cdn-images-1.medium.com/max/800/1*AbEg31EgkbXSQehuNJBlWg.png" align=right width=300 height=300>
landmarks on the face which is provided by the dlib shape_predictor. Each point corresponds to the point in the face. Since we are considered in only eyes and lips. We'll be drawing boxes around them only by using following points
- Lips -> width= P(54)-P(58), height = P(52)-P(57)
- Left Eye -> Radius = [P(39)-P(36)]/2
- Right Eye -> Radius = [P(45)-P(42)]/2

Since we know the cordinates we'll be able to draw boxes and circles around them.

<br>

## Workflow of Program

#### Libraries Needed  - Cv2, dlib, zmq, numpy 
<br>

- At first connections will be stablised by opening sockets from client side and binding it to server end and connect them using ip.
 - Now client's camera will be on and it'll start sending the frames by converting it to buffer form
 - At server side as the buffer is recived it is reconstructed into frame using numpy.
 - Now server performs all the detections and draws the boxes using dlib and cv2 and send back the frame to client using same buffer.
 - Again the client reconstructs frame from buffer and then displays it.

 ## Results
 <table align="center">
    <tr>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/raw.jpg" width=200 height=200></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/detected.jpg" width=200 height=200></td>
    </tr>
    <tr>
        <td><b>Image Sent to Server </b></td>
        <td><b>Image Received from Server </b></td>
    </tr>
</table>

<br>

### Authors's Contact
[![linkedin](https://github.com/anshumyname/anshumyname/blob/master/imgs/linkdin.jpg)](https://www.linkedin.com/in/anshuman-srivastava-84a0b3188/) &nbsp;&nbsp;&nbsp;
[![facebook](https://github.com/anshumyname/anshumyname/blob/master/imgs/fb.jpg)](https://www.facebook.com/anshuman.srivastava.9889) &nbsp;&nbsp;&nbsp;
[![mail](https://github.com/anshumyname/anshumyname/blob/master/imgs/gmail.jpg)](mailto:srivastavaanshuman33@gmail.com)  