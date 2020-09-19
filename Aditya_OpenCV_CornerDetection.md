## Corner Detection in OpenCV
Corner Detection is detecting corner points in an image. Basically the popular algorithms in OpenCV are as follows:
1. **Harris Corner Detection**
2. **Shi-Tomasi Corner Detection**

Let's see the basic intution behind corner detection:
  
In the animation below, there is a kernel or window which moves in particular alignment on the image. The image contains the shape on which the corners are to be detected.
  
![Animation1](Aditya_pics/Animation1.gif)
  
Here when the kernel moves we can see the intensity change in the kernel but in a particular axis either x-axis or y-axis. Here we can say that its an edge.
  
![Animation2](Aditya_pics/Animation2.gif)

As the kernel moves towards the corner, the intensity change is in different axes. Thus a corner is detected.
  
![Animation3](Aditya_pics/Animation3.gif)
