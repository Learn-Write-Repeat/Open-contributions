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

To summarize the ***ShapeDetector*** class, it is a class that we define to *detect* the shape of a **Contour**. The **constructor** has no role to play since the object of thus class *doesn't* need any **initialization**. The member function **detect(self , c)** takes a contour as an argument, processes it to determine the shape of the contour.

    
    class ShapeDetector:
    def __init__(self):
        pass
        
 
    def detect(self , c):
        shape = "unidentified"
        #Find the perimeter of the shape
        peri = cv2.arcLength(c , True)
        #Approximate the contours to get the number of vertices
        approx = cv2.approxPolyDP(c , 0.04 * peri , True)
        
        #Start detecting the shape based on the number of vertices
        #If the number of vertices is 3, its a triagle
        if len(approx) == 3:
            shape = "Triangle"
        #If the number number of vertices is 4, the shape can either be a square or a rectangle
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
        
The shape of the contour is initialised to be "unidentified". 
