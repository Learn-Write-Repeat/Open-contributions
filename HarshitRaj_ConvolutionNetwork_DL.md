# Covalution Neural Network
  Convolution Neural Network(**CNN**) is mainly used for Computer Vission beccause it is capable of extracting the main feature of image.
  It uses **Filters** to do that and since an image will have huge amount of features to train on, so normal neural network (Straight Forward) will     take more time to train and the no. of pararmeters to train on will increase exponentially.
  
  For example a image is of 1080p that means it'll have 1080 * 1080 pixels. Which is equal to 1166400, that means we have to train upon 1166400         features. In this the model the input layer itself will have 1166400 nodes and then the hidden layer should have equal or more nodes to process       the image and hidden layer will obviously have five to six layers to handle that big no. of feature and train it. This will take a long time to       train the model and the parameters will be too much to handle.
    
  To solve this problem **CNN** came into the picture. In this network the main part is **filters** which pass trough the image and filters the         importnat features from it like (horizontal edges or vertical edges, sharpening of image, bright side of the image and etc).
  It doesn't need huge amount of parameters to detect the main features of image. It only requires filters of certain size to convolute the image. 
  For exaple, lets take a matrix which represent a part of image and that matrix presents the edge of the image and also consider  fiter of size 
  3 * 3
  ![convolution layers](https://i.stack.imgur.com/uEoXw.gif)
  
  As we can see in the gif above the filter(AKA kernel) is used to map the information from the image part by part and store it in the output matrix.
  In this the kerne is of size of 3 * 3 and when it is traversing trough the image it will do the following steps,
  1. The kernel would first fit itself to the image matrix and take the first 3 * 3 sub_matrix to covalute.
  2. After selecting the sub matrix it does the multiplication of the sub matrix and filter, element wise and take sum of the product and that's the      value of sigle cell in the new matrix.
  for example if the selected sub matrix is 
  [[1,2,3],
    [4,5,6],
    [7,8,9]]
  and the kernel matrix is 
  [[1,0,0],
   [0,1,0],
   [0,0,1]]
   then calculation will be as follows,
   (1 * 1)+(2 * 0)+(3 * 0)+(4 * 0)+(5 * 1)+(6 * 0)+(7 * 0)+(8 * 0)+(9 * 1)=1+5+9=15
   So the cell value is 15.
   
   After claculating this the kernel will get shifted to next sub matrix.
   
   As you can see the gif above the kernel(filter) is getting shifted. So, how the filter is getting shifted? The answer to this is **stides**.
   **Strides** decide how to shift the filter on the image matrix. 
   
   If the value of stride is 1 then the kernel shift right side by one collumn and shift down by one row.
   
   If the value of stride is 2 then the kernel shift right side by two collumns and shift down by two rows.
   
   By defaul the kernel(filter) is situated at top-left corner of the image matrix.
   
   
   After calculating the value of all the sub_matrix with respect to the kernel the new matrix is filled with the values calculated.
   And as we can see that the sub_matrix of 3 * 3 is converted to one value (i.e. nine values after getting filtered is converted into 1 value).
   That means the new matrix will be smaller that the previous image matrix.
   This doesn't mean that we lost the data instead we have get deepen into the image and extracted some important feature from the large image.
   Well now the question comes in the mind that, how to define the size of new matrix(extracte matrix).We can find the size by a formulae,
   if the image matrix is of **(h * w)** and the kernel size is of the size **(hf * wf)** then the new matrix size will be of the size **(h-hf+1) *    (w-wf+1)**.
   
   So this was basically done in 2D image matrix which is a balck and white image in real-world. But what if the image is color imge that means        it'll have the R(red), B(blue), G(green) values and it'll be a 3 dimension matrix h * w * d. The 'd' value will be equal to 3. Since we are now    working on three colors RBG (Color image constitute of three main colors those are Red, Blue and Green).
   
   Now that the image matrix is 3 Dimensions the kernel(Filter) should also be a 3 Dimendsion matrix with same 'd' value.
   The image matrix shape is **(h * w * d)** then the kernel(filter) size will also be **(hf * wf * d)** and the new matrix will be of **(h-hf+1) *    (w-wf+1)**.
   
   [covolution with 3D](https://indoml.files.wordpress.com/2018/03/convolution-with-multiple-filters2.png?w=979)
   
   If the image feature is large or the image matrix is large Only one filter would not be of any help. We need no of filters and this will affect    the size and the value of new matrix.
   Before the image matrix and kernel(filter) matrix was in 3 dimension yet the new matri was in 2 Dimension
    
   
   
   
   
   
  
