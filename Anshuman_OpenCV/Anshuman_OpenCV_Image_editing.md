# Image Editing

OpenCV is vast library for using highly optimized functions and tools for the use of Image processing and editing which accleratess the speed and performance of different Computer Vision models and infrastructures. Here we'll be dealing with some of the basic Image editing steps which are provided by Cv2.
<br>
We'll deal with following types of Image editing -

- Basic Editing -
    -  Cropping
    -  Flipping
    -  Resizing

- Advance Editing -
    -  Thresholding
    -  Inversion
    -  Blur

Let's look at them at one by one

<br>

## Basic Editing
<br> 

### 1. Cropping 
Cropping refers to extracting a portion of image from of any size from the original image. The cropped image contains the required portion of the image rejecting the unwanted portion. <br>
This process helps in making the size of image small and thus 
speeding the process performed on the image 
<br>
<table align="center">
    <tr>
        <td><img src="https://github.com/anshumyname/Open-contributions/tree/master/Anshuman_OpenCV/images/Lenna_.png" width=200 height=200></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/tree/master/Anshuman_OpenCV/images/lena_crop.png" width=200 height=200></td>
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
        <td><img src="https://github.com/anshumyname/Open-contributions/tree/master/Anshuman_OpenCV/images/Lenna_.png" width=200 height=200></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/tree/master/Anshuman_OpenCV/images/horiz_flip.png" width=200 height=200></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/tree/master/Anshuman_OpenCV/images/vert_flip.png" width=200 height=200></td>
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
        <td><img src="https://github.com/anshumyname/Open-contributions/tree/master/Anshuman_OpenCV/images/small.png" ></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/tree/master/Anshuman_OpenCV/images/default.png"></td>
        <td><img src="https://github.com/anshumyname/Open-contributions/tree/master/Anshuman_OpenCV/images/large.png"></td>
    </tr>
    <tr>
        <td><b>Shrinked (128,128)</b></td>
        <td><b>Default (200,200)</b></td>
        <td><b>Enlarged (256,256)</b></td>
    </tr>
</table>

<br><br>

## Advance Editing
<br> 

## 1. Thresholding






