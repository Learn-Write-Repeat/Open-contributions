### contours
Contours are mathematical concept, it’s a connected line of points of inputs, for which a function have same output value. Like this, particular contour plot of, two features theta0 and theta1, that are input to a function, where values of function output are given by various colored lines. Each colored line is one output value of the function obtained by trying various combination of both input features along a single contour line.Now if we take this concept to image processing, and apply contours on images, it actually means selecting line of pixels have same value, and that line enclose a group of pixel values almost similar to the line pixels. In simple terms, Boundary! Yup, contours are boundaries of objects in an image.
### shape detection
We then load the image, we get the threshold of the image to have a black and white image, where the background is white and all the shapes are black.
From the black and white image we find the contours, so the boundaries of all the shapes.The shape will be detected on the basis of the number of sides it has.
### feature detection
SIFT (Scale-Invariant Feature Transform)
The way it gets scale invariant is by using image pyramids! After that keypoints (found via difference of gaussians) are localised to the subpixel and compared across the different scales. That's how you get scale invariance.
Keypoints are then removed according to a threshold, and then assigned orientations (with a 36 bin orientation histogram).
The 16x16 pixel neighbourhood around the keypoint are split into 4x4 size sub-blocks (16 in total), that are also given orientations as an 8 bin orientation histogram. That's how you get rotation invariance.
The feature are these keypoints with their neighbourhood pixel orientations rotated by the keypoint's specific orientation, represented as vectors! (The neighbourhood pixel sub-blocks are described in total by 128 orientation histogram bins. THIS is the feature, after you rotate them by the keypoint's overall orientation.)
### canny edge detection
The most famous tool to perform this task in OpenCV is the Canny filter. It is based on:
the gradient of the image (the difference between two adjacent pixels) a hysteresis filtering.
The hysteresis enables the selection of lines of adjacent pixels contrasting with their neighbors.The Canny filter thresholds can be tuned to catch only the strongest edges and get cleaner contours. The higher the thresholds, the cleaner the edges.
### face detection
The very first task we perform is detecting faces in the image or video stream. Now that we know the exact location/coordinates of face, we extract this face for further processing ahead.We will use a Face cascade and Eye cascade. You can find a few more at the root directory of Haar cascades. Note the license for using/distributing these Haar Cascades.Basically, it finds faces! We also want to find eyes, but, in a world of false positives

##### Thejaswin S
contact me through Thejas2002@yahoo.in
