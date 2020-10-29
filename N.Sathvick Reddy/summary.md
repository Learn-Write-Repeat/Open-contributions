In this module we have learnt about various actions which we can perform on images and videos.They are

1)Image Segmentation:

Image Segmentation is generally done using watershed algorithm by OpenCV.I have learnt how to segment objects which are mutually touching in an image using watershed algorithm.One great use of watershed algorithm is using it you can count the number of objects in an image even though they are touching each other.There are a series of steps to perform before applying watershed and we should also have our marker imagae ready to get a good result.

2)Contours:

Borders of objects are called as contours.They are very useful while we are working with shape anlysis, object detection and recognition.To find contours in an image first we need to convert into HSV format from BGR format.The contour points are found using cv2.findContours(). Later using drawContours() we plot all the contoural points using a different colour preferably.

3)Finding an object and marking its extreme points:

This as an advancement to finding the contoural points as we need to find extreme points along the contour.After loading the image we will perform thresholding and find contours and draw the outline with a different colors.Extreme top, bottom,left and right points are found and marked on the outline which is the final output.

4)Specific patterns in images:

As we know whenever we need to find patterns or shapes we make use of contours.First the loaded image is converted to grayscale , blurred and thresholded.Contours are found and stored. The weighted average of the image pixels' intensities, usually chosen to have some attractive property is found which helps in finding the centroid of the given contour. Then based on the number of sides and ratio of sides of contours we can name each contour as names of shapes.

5)Getting Image features:

Feature detection is easy for a human brain as it is done without any delay. But for a computer to find features present in an image it we need to first find it in an image which can be used to find it in other images this is called feature detection and describing each feature in a word is called feature description.Nearest Neighbors concept will be useful for finding the features.

6)Face Detection

Face Detection can be easily done using a haar classifier. Haar Classifier is a function which is trained with and without face such that it can find a face when it is present an image based on its training.Once the face is detecte we ususaly draw a box around the face in the image to highlight it.In the same way eyes also can be detected using a pre trained classifer. This can be helpful in detecting drowsiness in drivers based on this classifier.

7)Flask

 Flask is a web application framework written in Python.It is very light. It helps us to create dynamic web applications. It facilitates creation,development and publishing of web applications.Flask helps programmers to give their machine learning or computer vision modules a UI and also can test them on their local machines.It makes the code to look like a product and as it is made in python we can use the in built functions to do most of the tasks while making the applications
                                                                                                                                                        
