# OpenCV

OpenCV is a huge open-source library which is used for computer vision and image processing. It also plays an important role in real-time operations.It can process images and videos to identify objects, faces, or even the handwriting of a human.It has many in built functions which make our work a bit easy.

![](https://developer.nvidia.com/sites/default/files/akamai/cuda/images/product_logos/OpenCV_Logo_340.jpg)

## Installing Opencv  ##
   pip install opencv-python

# FACE DETECTION USING WEBCAM(DISPLAYS THE PERCENTAGE OF TIME A FACE WAS DETECTED)

Face Detection is a process in which faces are identified in images or videos. Face detection can be applied in many places for security and surveillance reasons.Face Detection is basic step after which we can perform other complex activities such as face recognition, drowsiness detection, findig the emotion etc...

![](https://raw.githubusercontent.com/cjekel/cjekel.github.io/master/assets/2017-05-01/faceBoxed357px-Obama_portrait_crop.jpg)

Face detection in live video or saved videos is similar to that of face detection in a photo.We are going to detect face in real time using the webcam of our laptop.There are many ways to detect faces but using the opencv package along with a haarcascade file is the simplest of all.Here we are going to use ![Haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml). This helps us to detect the face easily in a video or image.
Once the face is detected we generally draw a box around the box and as we move our face in the webcam the rectangular box also moves as it is drawn using the coordinates of the face in real time.

After we end the video we will also a get a percentage which tells us the amount of time a face was detected.If a face was detected during the entire time it displays as 100% if not it displays the percentage of time it was displayed, here when I say face it implies to frontal face as we are using a frontal face cascade file.
The additional feature of displaying the percentage of time face was detected will be helpful in online classes where we can fix  a threshold percentage and if a students face was detected for more than that threshold he is considered as present and if not as absent.

Author: N.Sathvick Reddy

Email: Sathvicknarahari@gmail.com
