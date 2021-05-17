This is a file to detect the user's face.

Steps:-
1. import libraries
2. load our classifier(harrcascades)
3. define the fuction that will detect the face in the image(convert from BGR to grayscale) and return the cropped face
4. we will take the im=nput from our webcam
5. the function will detect the face and will store it in a directory (for training)
6. now coming to the training part- we first set the data paths, then we load in our images from the directory saved above
7. we define our model (LBPHFaceRecognizer - LocalBinaryPattern)
8. then train it
9. finally our prediction/running part- first we make a function to take the images, convert to grayscale, resize
10. also we load "haarcascade" facial detector to detect the face and then apply our model to match the face to previously trained face
11. we take the inputs from our webcam
12. detect faces - apply model to match- return results- show results on screen
