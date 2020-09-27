# Image Filtering
<p>
<b>by Om Rastogi  </b>  
<a href="https://twitter.com/OmRastogi"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitter.svg"  alt="Om's Logo" width="15" height="15"></a> 
<a href="https://medium.com/@omrastogi"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/medium.svg"  alt="Om's Logo" width="15" height="15"></a> 
<a href="https://www.linkedin.com/in/om-rastogi-a886b4b2/"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg"  alt="Om's Logo" width="15" height="15"></a> 
<a href="https://omrastogi.github.io/omrastogi/index.html"><img src="https://omrastogi.github.io/omrastogi/images/logo.png" alt="Om's Logo" width="22" height="15"></a> 
</p>

Filtering recalculates each pixel after operating it with a mask or kernal. 
It is used for blurring, sharpening, edge detection and many more purposes. 
There are two component while convoluting:
1. Image 
2. Kernal - matrix of size nxn (where n is always odd). The sum of the whole matrix is needed to be zero or near zero. 
To perform masking the kernal matrix is convoluted over the image. 
### Convolution
<br>
<img src = "https://mlnotebook.github.io/img/CNN/convSobel.gif" alt="Animation">
<br>
In mathematics convolution is defined as the sum of the product of the two functions after one is reversed and shifted.
However, since in masking reversing a function doesn't make a differece therefore simple product of each element is sumed to save computation. 
<b>Formula for convolutional Network:</b><br>
<img src = "https://pages.jh.edu/~bmesignals/New/disc_conv_eqn.gif" alt = "formula">
<br>
<img src = "https://miro.medium.com/max/464/0*e-SMFTzO8r7skkpc" alt = "convolution operation">

## Implementation in OpenCv Python 
The method cv2::filter2d is used to apply any custom image filter. 
```python 
dst = cv.filter2D(src, ddepth, kernel [, dst[, anchor[, delta[, borderType]]]]	)
```
### Parameters 
**src, ddepth and kernal are essential parameter** <br> 
**src**	       `:input image.` 

**ddepth**     `:desired depth of the destination image, see combinations.`

**kernel**     `:convolution kernel (or rather a correlation kernel), a single-channel floating point matrix; if you want to apply different kernels to different channels, split the image into separate color planes using split and process them individually.`

*anchor*    `:anchor of the kernel that indicates the relative position of a filtered point within the kernel; the anchor should lie within the kernel; default value (-1,-1) means that the anchor is at the kernel center.`

*delta*	     `:optional value added to the filtered pixels before storing them in dst.`

*borderType* `:pixel extrapolation method, see BorderTypes. BORDER_WRAP is not supported.` 


## Application 
### Given the following image we'll discuss the effects of kernel
<img src = "https://upload.wikimedia.org/wikipedia/commons/5/50/Vd-Orig.png" alt = "img">

<b>Sharpen</b> 
<br><br>
<p>
<img src ="https://wikimedia.org/api/rest_v1/media/math/render/svg/beb8b9a493e8b9cf5deccd61bd845a59ea2e62cc" alt="kernal" > 
<img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Vd-Sharp.png" alt="img" >
</p>
<br><br>
<b>Average Blurring</b> 
<br><br>
<p>
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/91256bfeece3344f8602e288d445e6422c8b8a1c" alt="kernal" >
<img src="https://upload.wikimedia.org/wikipedia/commons/2/28/Vd-Blur1.png" alt="img" >
</p>
<br><br>
<b>Edge Detection </b>
<br><br>
<p>
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/f800ad5f76b6c26c729ff0c1fef44284d7cade7a" alt="kernal" >
<img src="https://upload.wikimedia.org/wikipedia/commons/6/6d/Vd-Edge3.png" alt= "img" >
</p>
<br><br>
This is one of the most powerful technique in the arsenal of image processsing, 
present day Convoutional models are based on this operations to find different features in the network.
