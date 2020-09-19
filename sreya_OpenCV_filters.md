## **Image filtering**

* We use filters to smoothen the image,remove noises,blur image , find edges of objects in image
* There are 2 types of filters:<br>
  - High pass filters : for finding edges
  - Low pass filters  : for smoothening image
* Filtering is done by convoluting image with filter we provide
* there are many filters for different purposes
* Filters listed here :
```
  * Basic filter function - cv2.filter2D()
  * Low pass filters
    - Averaging filter 
    - Median filter 
  * High pass filters:
    - Laplacian filter 
    - Sobel filter
```
#### **1. cv2.filter2D()**
* This function is used to customize your own filter instead of using existing filters
* **syntax:**<br>
` cv2.filter2D(img,ddpeth,filter) `<br>
**explaination:**<br>
  * img - image which we want to convolute with filter 
  * ddpeth - it specifies about the depth of output image , keep it '-1' to make the depth of output equal to depth of input image
  * filter - which we are using
#### **2. cv2.blur() - Average filtering**
* It is a low pass filter used for blurring ( smoothening image ) 
* It takes the average of all pixels in filter area and replaces the central pixel value with the calculated average 
* **syntax:**<br>
` cv2.blur(img,filter_size) `<br>
**explaination:**<br>
  * img - image which we want to convolute with filter 
  * filter_size - (a,a) size of the filter you want to use ,each element in the filter is 1/a^2
#### **3. cv2.medianBlur() - Median filtering**
* Low pass filter
* This is used for smoothening image by preserving small deatils 
* It calculates median of all the pixels under the filter size and the central pixel is replaced with this median value
* **syntax:**<br>
` cv2.medianBlur(img,filter_size) `<br>
**explaination:**<br>
  * img - image which we want to convolute with filter 
  * filter_size -size of the filter
#### **4. cv2.Laplacian() - laplacian filtering**
*   High pass filter used for edge detection 
*   we know that image is 2D picture and will have both horizontal features and 
vertical features , laplcian filter detects both dimensional features
* **syntax:**<br>
` cv2.medianBlur(img,ddepth,ksize) `<br>
**explaination:**<br>
  * img - image which we want to convolute with filter
  * ddpeth - it specifies about the depth of output image , keep it '-1' to make the depth of output equal to depth of input image
  * ksize -size of the filter
#### **5. cv2.Sobel() - sobel filtering**
*   High pass filter used for edge detection 
*   we know that image is 2D picture and will have both horizontal features and 
vertical features , sobel filter can be used to detect features in specific dimension
* **syntax:**<br>
` cv2.Sobel(img,ddepth,dx,dy,ksize) `<br>
**explaination:**<br>
  * img - image which we want to convolute with filter
  * ddpeth - it specifies about the depth of output image , keep it '-1' to make the depth of output equal to depth of input image
  * dx,dy - this specify which dimension who want to check for : 0,1 - horizontal ; 1,0 - vertical
  * ksize -size of the filter
<br.<br>

My contact details <br>
gmail : [vishnusreya15@gmail.com](mailto:vishnusreya15@gmail.com) <br>
linkedin : [sreyaReddy](https://www.linkedin.com/in/sreya-reddy-2a0b96184/)




