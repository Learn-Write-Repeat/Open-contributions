# Basic functions in OpenCV

There are so many fucntions present in OpenCV for image processing.
now we will learn various operations we can perform on the image for image processing one by one.

#### list of operations:
    1.Grayscaling
    2.Image Translations
    3.Rotation,Scaling,cropping and Re-sizing
    4.Arithmetic and bitwise Operations
    5.Sharpening, Thresholding, Dilation
    6.Edge detection

## 1. Greyscaling

Greyscaling is the process of converting an image from  format RGB, CMYK, HSV, etc. to shades of grey. the greyscale image is varies between complete white and complete black.<br>
##### for the above operation cv2.cvtColor() this function is used.

### Applications Of Greyscaling:
1. There are so many algorithms that can customized to work only with the greyscaled images for e.g. Canny edge detection function pre-implemented in OpenCV library works on Grayscaled images only.
2. There is dimensional reduction in greyscale image as RGB image has 3 channels and greyscaled image has only 1 channel.


## 2. Translation 
Translation is the process of shifiting image from one location to another location.<br>
this can be done using transformation matrix

<br>



