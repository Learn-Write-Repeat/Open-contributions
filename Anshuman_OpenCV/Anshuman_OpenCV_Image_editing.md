
# __Image Editing__

OpenCV is vast library for using highly optimized functions and tools for the use of Image processing and editing which accleratess the speed and performance of different Computer Vision models and infrastructures. Here we'll be dealing with some of the basic Image editing steps which are provided by Cv2.
<br>
We'll deal with following types of Image editing -

- Basic Editing -
    -  Cropping
    -  Flipping
    -  Resizing

- Advance Editing -
    -  Grayscaling & Thresholding
    -  Blur
    - Smoothening

Let's look at them at one by one

<br>

## __Basic Editing__
<br> 

### 1. Cropping 
Cropping refers to extracting a portion of image from of any size from the original image. The cropped image contains the required portion of the image rejecting the unwanted portion. <br>
This process helps in making the size of image small and thus 
speeding the process performed on the image 
<br>
<table align="center">
    <tr>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/Lenna_.png" width=200 height=200></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/lena_crop.png" width=160 height=200></td>
    </tr>
    <tr>
        <td><b>Original Image</b></td>
        <td><b>Cropped Image</b></td>
    </tr>
</table>

### 2. Flipping
Flipping is just taking the mirror image of the original image. It is usually used when we have to create more data images from the existing ones. We can flip the image either taking x axis or y axis as reference. Here is the example of both operations.
<br>
<table align="center">
    <tr>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/Lenna_.png" width=200 height=200></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/horiz_flip.png" width=200 height=200></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/vert_flip.png" width=200 height=200></td>
    </tr>
    <tr>
        <td><b>Original Image</b></td>
        <td><b>Horizontal Flipped</b></td>
        <td><b>Vertical Flipped</b></td>
    </tr>
</table>

### 3. Resizing
Resizing has been always one of the most important steps in image processing. It can be both used to enlarge and shrink images. The Cv2 library provides different mehtods of resizing Some of them are 

- cv2.INTER_NEAREST - uses near neigbour pixels for calculating new pixel value.
- cv2.INTER_CUBIC - uses bicubic interpolation 
- cv2.INTER_LINEAR - *(default)* uses linear interpolation , usually used while zooming image
- cv2.INTER_AREA - uses some resampling with pixel area relation, usually used while shrinking image

For more methods [click here](https://docs.opencv.org/master/da/d54/group__imgproc__transform.html#ga5bb5a1fea74ea38e1a5445ca803ff121)

<br>
<table align="center">
    <tr>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/small.png" ></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/default.png"></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/large.png"></td>
    </tr>
    <tr>
        <td><b>Shrinked (128x128)</b></td>
        <td><b>Default (200x200)</b></td>
        <td><b>Enlarged (256x256)</b></td>
    </tr>
</table>

<br><br>

##  __Advance Editing__
<br> 

### 1. Grayscaling & Thresholding
**Grayscaling** refers to converting the RGB image to B/W i.e. converting the 3 channels of RGB to single channel.
By converting the image to gray one can perorm thresholding and morpholgy on the images. 

<table align="center">
    <tr>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/text.png" width=200 height=200></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/gray_text.png" width=200 height=200></td>
    </tr>
    <tr>
        <td><b>Original Image</b></td>
        <td><b>Grayscaled Image</b></td>
    </tr>
</table>

<br> 

**Thresholding** is a technique used to separate foreground with background . Here a threshold is set *(by default 128)* and pixel values above it are converted to 255 (pure white) and below it are converted to 0 (pure black).
This is simple thresholding. There are different types of thresholding methods too.

- Simple Thresholding - Threshold based 0 & 255 mapping 
- Adaptive Thresholding - Varying threshold depending upon neigboring pixels
- Otsu's Binarization - used in bimodal images (where we have greater color density in more than one spot).

<table align="center">
    <tr>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/threshold.png" width=200 height=200></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/adapt_threshold.png" width=200 height=200></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/otsu_thresh.png" width=200 height=200></td>
    </tr>
    <tr>
        <td><b>Simple Threshold</b></td>
        <td><b>Adaptive Threshold</b></td>
        <td><b>Otsu Threshold</b></td>
    </tr>
</table>
<br>

### 2. Blur
Blurred images are useful for removing noise and high frequency content present in ihe image. Thus by blurring edges we try to denoise the image for further processing. For seeing effects of blur operation we'll take this pic.

<<table align="center">
    <tr>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/face.png" width=230 height=200></td>
    </tr>
    <tr>
        <td><b>Source Image</b></td>
    </tr>
</table>

In general there are four types of blurring done for the images.

- Averaging - runs a kernel of some size k and takes average of all k*k elements and replaces the central pixel by it.
- Gaussian Blur - similar to previous method but what differs is that this method uses gaussian kernel with given SD and mean. 
- Median Blurring - takes the median of all of k*k pixels under the k-size kernel, used when we have salt-and-pepper noise
- Bilateral Filter - Similar to Gaussan blur but also takes in account the pixel intensity differences and thus it is a slow operation as compared to others.


<table align="center">
    <tr>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/blur.png" width=230 height=200></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/blur_gauss.png" width=230 height=200></td>
    </tr>
    <tr>
        <td><b>Average Blur</b></td>
        <td><b>Gaussian Blur</b></td>
    </tr>
    <tr>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/blur_median.png" width=230 height=200></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/blur_bilateral.png" width=230 height=200></td>
    </tr>
    <tr>
        <td><b>Meidan Blur</b></td>
        <td><b>Bilateral Filtering</b></td>
    </tr>

</table>


### 3. Smoothening
Smoothening is nothing but a kernel operation which is convolved with the original image to produce a bit sharper image than before.

<table align="center">
    <tr>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/blurred.png" width=200 height=200></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/sharpen.png" width=200 height=200></td>
    </tr>
    <tr>
        <td><b>Source Image</b></td>
        <td><b>Sharpened Image</b></td>
    </tr>
</table>

<br>

### Example of Image Preparation 

Here is an examle of image which is processed step by step to prepare for the input feed to any CV model.

- Source images is resized to 64x64
- Converted to Grayscale
- Applied Thresholding (any type)
- Applied a smoothen filter

<br>

<center><img src="https://github.com/anshumyname/Open-contributions/blob/master/Anshuman_OpenCV/images/example.png" ></center>




##   Author's Contact 
[![linkedin](https://github.com/anshumyname/anshumyname/blob/master/imgs/linkdin.jpg)](https://www.linkedin.com/in/anshuman-srivastava-84a0b3188/) &nbsp;&nbsp;&nbsp;
[![facebook](https://github.com/anshumyname/anshumyname/blob/master/imgs/fb.jpg)](https://www.facebook.com/anshuman.srivastava.9889) &nbsp;&nbsp;&nbsp;
[![mail](https://github.com/anshumyname/anshumyname/blob/master/imgs/gmail.jpg)](mailto:srivastavaanshuman33@gmail.com)  






















