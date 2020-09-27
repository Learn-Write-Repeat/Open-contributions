# Convolution Matrix

Masking recalculates each pixel after operating it with a mask or kernal. 
It is used for blurring, sharpening, edge detection and many more purposes. 
There are two component while convoluting:
1. Image 
2. Kernal - matrix of size nxn (where n is always odd). The sum of the whole matrix is needed to be zero or near zero. 
To perform masking the kernal matrix is convoluted over the image. 
### Convolution
<br>
<img src = "https://miro.medium.com/max/464/0*e-SMFTzO8r7skkpc" alt = "convolution operation">

In mathematics convolution is defined as the sum of the product of the two functions after one is reversed and shifted.
However, since in masking reversing a function doesn't make a differece therefore simple product of each element is sumed to save computation. 
<b>Formula for convolutional Network:</b><br>
<img src = "https://pages.jh.edu/~bmesignals/New/disc_conv_eqn.gif" alt = "formula">

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
