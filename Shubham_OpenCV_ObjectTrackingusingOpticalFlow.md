<p >
   <a href="mailto:srajput1912000@gmail.com">
    <img src="https://img.shields.io/badge/-srajput1912000@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:srajput1912000@gmail.com">
   <a/>
   <!--  <a href="https://github.com/Shubham0Rajput/Shubham0Rajput"> 
    <img src="http://okokcoolokok.glitch.me/badge?page_id=Shubham0Rajput.Shubham0Rajput"> -->
   <a/>
   <a href="https://twitter.com/_Shubham0Rajput">
    <img src="https://img.shields.io/badge/-@_Shubham0Rajput-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/_Shubham0Rajput">
   <a/>
   <a href="https://t.me/Shubham0Rajput">
    <img src="https://img.shields.io/badge/-Shubham0Rajput-blue?style=flat-square&logo=Telegram&logoColor=white&link=https://t.me/Shubham0Rajput">
  <a/>
  <a href="https://www.linkedin.com/in/shubham0rajput/">
    <img src="https://img.shields.io/badge/-Shubham0Rajput-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/shubham0rajput/">
  <a/>
</p>

# Object Tracking using Optical Flow with OpenCV
In this we are going to track the flow of object in video with OpenCV.


### Shi-Tomasi corner detection
---------------------------------
In this, the main basic function was given "goodFeaturesToTrack()" is main motive was to mark the good corner's. It requires grayscale images for its processing. Its one of the
best corner detection method known. The detection of this process looks like this:
![image](https://github.com/Shubham0Rajput/Open-contributions/blob/master/Shubham_OpenCV/shitomasi_block1.jpg)


### Lucas-Kanade Optical Flow
---------------------------------
An differential method used for flow detection,from comparing the pixel from nearby it estimates the flow. Method fails when the motion is big or large which was later on 
changed to pyramid multi-scaled method for that purpose. Its best for slow and consecutive flow  



### Dense Optical Flow
---------------------------------
This computes the optical flow for every pixel of the frame in vector form, which may be responsible for its slow speed but leading to a better accurate result.
It can be used for detecting motion in the videos. 
It computes the optical flow for all the points in the frame, it gets a 2-channel array with optical flow vectors. Its color code the result for better visualization of the output.




Step 1. Download
---------------------------------
* for download with python
  ```
  pip install opencv-python
  ```
* for download with [Anaconda](https://www.anaconda.com/products/individual)
  ```
  conda install -c conda-forge opencv
  ```
* In-case error comes try 
  ```
  pip install pip
  ```
  this is when your pip is old. Also can use pip command in Anaconda


Step 2. Copy Video
---------------------------------
Download and Add these videos [video.mp4](https://github.com/Shubham0Rajput/Open-contributions/blob/master/Shubham_OpenCV/video.mp4), [video1.mp4](https://github.com/Shubham0Rajput/Open-contributions/blob/master/Shubham_OpenCV/video1.mp4) 
into your system.


Step 3. Open Code
---------------------------------
[Code](https://github.com/Shubham0Rajput/Open-contributions/blob/master/Shubham_OpenCV_ObjectTrackingUsingOpticalFlow.ipynb) 
copy this code or download and run it with Jupyter Notebook by
```
jupyter notebok
```
type this in Anaconda Promt then locate the code and open it

Step 4. Run
---------------------------------
To run the code tap on Run or press Alt+Enter to run it.



Result
---------------------------------
### Result of Lucas Kanade Optical flow
![RESULT](https://github.com/Shubham0Rajput/Open-contributions/blob/master/Shubham_OpenCV/Lucas-Kanade%20optical%20flow.gif)


### Result of Dense Optical Flow
![RESULT](https://github.com/Shubham0Rajput/Open-contributions/blob/master/Shubham_OpenCV/Dense%20Optical%20Flow.gif)
