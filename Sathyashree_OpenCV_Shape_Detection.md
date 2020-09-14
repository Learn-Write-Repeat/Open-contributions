## Shape Detection

### Introduction:

Basically ***Shape Detection*** is nothing but **finding** different shapes in an image and **identifying** them. Using OpenCV, computers can be made able to detect shapes in an image by feeding them with some information and applying certain conditions and allow them to act based on the decision. This process involves *multi-steps*.

- *Installing* ***pip*** and ***imutils*** **packages**.
- *Importing* the necessary **libraries**.
- *Creating* the ***ShapeDetector*** **class**.
- *Loading* and *processing* the image and *finding* the contours.
- *Finding* the **center of each contour** and detecting the shape.
- *Displaying* the **output image**.

### Code Description:

Now, let's dive into the actual code of the topic. 

#### *Installing* ***pip*** and ***imutils*** **packages**:

The below-stated statements enable the user to *install* **pip** and **imutils** packages in the **conda environment**.

    conda install pip
    pip install imutils
    
#### *Importing* the necessary **libraries**:

Coming to the libraries that are used in this procedure, one needs to import **cv2** and **imutils**.

    import cv2
    import imutils
 
#### *Creating* the ***ShapeDetector*** **class**:

The tricky part of the code starts. Let's start coding!!!

To summarize the ***ShapeDetector*** class, it is a class that we define to *detect* the shape of a **Contour**. The **constructor** has no role to play since the object of thus class *doesn't* need any **initialization**. 

    class ShapeDetector:
        def __init__(self):
            pass
        
 The member function **detect(self , c)** takes a contour as an argument, processes it to determine the shape of the contour. The shape of the contour is initially "unidentified". Then, the **perimeter** of the contour is calculated using the *cv2.arcLength()* function. Then, the contour is **approximated** using the *cv2.approxPolyDP()* function that takes the contour as the first argument and the second parameter is normally in the range of **1-5%** of the original perimeter of the contour. The approximation is based on the idea that a *series of short line segments* can approximate a **curve** and the resulting curve consists of a **subset of the originally defined points**. This *approximation* gives us the **number of vertices**.
 
        def detect(self , c):
            shape = "unidentified"
            peri = cv2.arcLength(c , True)
            approx = cv2.approxPolyDP(c , 0.04 * peri , True)
 
 Once the number of vertices are known, the shape identification process is easier and based on few *conditions*. The series of conditions include checking if the contour has *3 vertices or 4 or 5 or none*. *3* vertices represent that the shape is a *Triangle*; *4* vertices mean its a *Rectangle* or a *Square*; *5* means its a *Pentagon*; *none* inflicts the idea that it should be a *circle*.
    
        if len(approx) == 3:
            shape = "Triangle"
        elif len(approx) == 4:
            #Draw an approximate rectangle around the contours 
            (x , y , w , h) = cv2.boundingRect(approx)
            #Calculate the ratio of width to height
            av = w / float(h)
            #If the ratio is approximately equal to 1, then the shape is a square, else a rectangle
            shape = "Square" if av >= 0.95 and av <= 1.05 else "Rectangle"
        #If the number of vertices is 5, its a pentagon
        elif len(approx) == 5:
            shape = "Pentagon"
        #If the shape is none of the above, then its a circle
        else:
            shape = "Circle"
        #Return the shape of the object
        return shape

The idea behind determining if the shape is a square or a rectangle is that the **ratio** of the *width to the height* of a **square** is **approximately equal to 1**. An **approximated rectangle** is drawn around the contoural points using the *cv2.boundingRect()* function and then, the *ratio* of the width to the height is found out.  If the value of the *ratio falls around 1*, then the shape is a *Square*, else a *Rectangle*.
