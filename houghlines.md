This model is made to detect lane lines on the road from the POV of a car
This is a very simple model and with little tweaking can give excellent results

Steps:-
1. import the libraries
2. define the input video
3. define the frame to be predicted on
4. convert the color from BGR to HSV (for easier manipulation)
5. set the approximate lane line colors (mostly yellow)
6. crate a mask using our defined colors (high_yellow to low_yellow)
7. detect edges using canny edge detection(taking in our mask)
8. use the houghlinesP method to detect lanes (taking in our edges)
9. mask the lane lines on the input video 
