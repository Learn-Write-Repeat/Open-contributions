# Covalution Neural Network
  Convolution Neural Network(**CNN**) is mainly used for Computer Vission because it can extract the main feature of the image.
  It uses **Filters** to do that, and since an image will have a vast number of features to train on, a regular neural network (Straight Forward)     will take more time to train, and the no. of parameters to train on will increase exponentially.
  
  For example, an image is 1080p, which means it will have 1080 * 1080 pixels. Which is equal to 1166400, which means we have to train upon 1166400   features. In this model, the input layer itself will have 1166400 nodes, and then the hidden layer should have equal or more nodes to process the   image, and the hidden layer will have five to six layers to handle that big no. of feature and train it. This will take a long time to train the   model, and the huge no. of parameters will be hard to handle.
    
  To solve this problem **CNN** came into the picture. In this network, the central part is **filters**, which pass through the image and filter the essential features from it like (horizontal edges or vertical edges, sharpening of the image, the bright side of the image, etc.).
  It does not need a huge amount of parameters to detect the main features of the image. It only requires filters of a specific size to convolute the image. 
  For example, let us take a matrix that represents a part of the image, and that matrix presents the edge of the image and also consider  filter of size 
  **3 * 3**.
  ![convolution layers](https://i.stack.imgur.com/uEoXw.gif)
  
  As we can see in the gif above, the filter(AKA kernel) is used to map the information from the image part by part and store it in the output matrix.
  In this, the kerne is of the size of 3 * 3, and when it is traversing through the image, it will do the following steps,
  1. The kernel would first fit itself to the image matrix and take the first 3 * 3 sub_matrix to convolute.
  2. After selecting the submatrix, it does the multiplication of the submatrix and filter, element-wise and take a sum of the product, and that is the value of the single cell in the new matrix.
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
   
   After claculating this the kernel will get shifted to next submatrix.
   
   As we can see in the gif above, the kernel(filter) is getting shifted. So, how the filter is getting shifted? The answer to this is **strides**.
   **Strides** decide how to shift the filter on the image matrix. 
   
   If the stride value is one, the kernel shifts right side by one column and shifts down by one row.
   
   If the stride value is two, the kernel shifts right side by two columns and shifts down by two rows.
   
   By default, the kernel(filter) is situated at the top-left corner of the image matrix.
   
   
   After calculating the value of all the submatrix with respect to the kernel, the new matrix is filled with the values calculated.
   Furthermore, as we can see that the submatrix of 3 * 3 is converted to one value (i.e. nine values after getting filtered is converted into one value).
   That means the new matrix will be more petite than the previous image matrix.
   This does not mean that we lost the data; instead, we got deeper into the image and extracted some important features from the large image.
   Well, now the question comes to mind that, how to define the size of a new matrix(extracted matrix). We can find the size by a formula,
   if the image matrix is of **(h * w)** and the kernel size is of the size **(hf * wf)** then the new matrix size will be of the size **(h-hf+1) *    (w-wf+1)**.
   
   So this was done in a 2D image matrix, a black and white image in the real world. However, what if the image is a colour image? That means it will have the R(red), B(blue), G(green) values, and it will be a three-dimension matrix h * w * d. The 'd' value will be equal to 3 since we are now working on three colours RBG (Color image constitutes three primary colours: Red, Blue and Green).
   
   Now that the image matrix is 3 Dimensions, the kernel(Filter) should also be a 3 Dimension matrix with the same 'd' value.
   The image matrix shape is **(h * w * d)** then the kernel(filter) size will also be **(hf * wf * d)** and the new matrix will be of **(h-hf+1) *    (w-wf+1)**.
   
   ![covolution with 3D](https://indoml.files.wordpress.com/2018/03/convolution-with-multiple-filters2.png?w=979)
   
   If the no. of the image feature is large, or the image matrix is large, only one filter would not help. We need more no. of filters, and this will affect the size and the value of the new matrix.
   Before, the image matrix and kernel(filter) matrix was in 3 dimensions, yet the new matrix was in 2 Dimension but now if we increase the no. of filters, then the dimension of the new matrix will also change, as we can see in the above figure we have used two filters of size **3 * 3 * 3**
   on the image matrix of **6 * 6 * 3** so the size of new matrix is **(6-3+1) * (6-3+1) * (no. of filters used)=4 * 4 * 2**.
   
  
    
   
   
   
   
   
  
