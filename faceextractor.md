This is basically the first part of the entire face detection model
Here we simply take in our input image - detect faces - extract them - show bounding box around them

Steps:-
1. Load in haarcascade face/eye classifier (our detection algorithm)
2. define a function that will - convert the image to grayscale, detect the faces(by applying our classifier) and draw bounding box
3. we start our webcam for input
4. run the function over the input
5. show the results on screen
