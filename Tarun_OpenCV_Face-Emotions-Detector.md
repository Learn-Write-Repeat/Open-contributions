# **Face Emotions Detector**
    by Tarun Krishnan
 Follow me on
   * Linkedin : https://www.linkedin.com/in/tarunkrishnan2000/
   * Github : https://github.com/tarun36rocker?tab=repositories
   -------------------------------------------------------------
 Now on to This Amazing and Simple Project that I made !
      
    The MAIN AIM was to try to understand if a computer can understand human emotions . Think about it this way ,
    computers are REALLY smart when it comes to crunching down numbers or even trying to find correlations in 
    datasets that they have never seen before in just a few minutes or hours! Something which humans study their whole lives for !
    So that really was the purpose of this project , to see if just by providing few images if a computer
    can understand basic human emotions , something which even humans find difficult to understand !
    
    WHERE can we use this project ? This project can be used in every field possible to be honest ! It can be used 
    to detect workplace mannerisms , observe the reactions of people while viewing your product and list goes
    ON AND ON !!
 So lets begin !   
    
 ![alt text](https://github.com/tarun36rocker/Open-contributions/blob/master/pic1.png)
    Just like how we need to brush every morning , we need to import few key modules that are required for the WHOLE
    program to run succesfully
    
   * Sequential :: This is the base/framework that you we will be using to integrate the different layers of the Neural Network !
   * Conv2D , MaxPooling2D , Flatten , Dense :: The above four lines are the different "Layers" that will be used in our Deep Learning model. 
   * ImageDataGenerator :: I will explain this very important function when we get to that part of the code !
   
    Now it's time to build our DEEP LEARNING/NEURAL NETWORK Model .   
  ![alt text](https://github.com/tarun36rocker/Open-contributions/blob/master/pic2.png)
   * Sequential :: This is the base or framework on which your model is built on
   * Conv2D , MaxPooling2D :: Are the first two layers that we are using in this model ,
   If you noticed , we are adding these two layers again . WHY ?
   The simple answer is more the layers , the more the network gets to understand , however just because we add more layers
   doesnt necessarily mean that it will always help with our model's accuracy . Sometimes the model may tend to [Overfit](https://www.investopedia.com/terms/o/overfitting.asp#:~:text=Overfitting%20is%20a%20modeling%20error,in%20the%20data%20under%20study.),
   so you have to be careful while adding more layers , for our model as we have a limited data set , 2 layers should suffice .
   * Flatten :: is the third layer we will be using which we will be using which is basically compressing our data to suit our model 
   * Dense :: We have 2 DENSE layers , the first dense layer connects to the ACTIVATION FUNCTION which is responsible for transforming
   the summed weighted input from the node into the activation of the node or output for that input ( very high level , I know ! )
   The second Dense layer helps in finally providing the OUTPUT in the form of a list which we will later observe !
   * compile :: Finally we are compiling all the different layers together and forming our MODEL , we will be testing our data
   on 'ACCURACY' and  basing our loss on 'Categorical_crossentropy' which is a method used when we have more than 2 types (BINARY) data
   
    Now Lets start builing our dataset !But before that , we need to create some folders !
    Our folders should be arranged in the following format because otherwise the model
    may not be able to train based on the categories correctly otherwise ! You have to ensure that there is main 'dataset' folder and in 
    that there are 3 subfolders -
    1)single_pred - which will be used to check if the model is working after compiling the model
    2) test_set - folder used to contain the test data 
    3) training_data - folder used to contain the training data
    
    Now inside these subfolders:
    1)single_pred - choose random pictures to evaluate your model
    2)test_data and training_data has to have 5 sub folders as seen in the pictures , where each folder will stand for their respective
    cateogires
    Inisde each of these emotions folders will contain the pictures or data that is pertailing to the category of the emotion 
    that it is supposed to represent
   ![alt text](https://github.com/tarun36rocker/Open-contributions/blob/master/pic3.png)
   ![alt text](https://github.com/tarun36rocker/Open-contributions/blob/master/pic4.png) 
   ![alt text](https://github.com/tarun36rocker/Open-contributions/blob/master/pic5.png)
    Now that we have created our folders , you might be asking how do we get this data ?
    The simple answer is we will be SCRAPING our data using BingImageCrawler !
    
   ![alt text](https://github.com/tarun36rocker/Open-contributions/blob/master/pic6.png) 
    As you can see from the above picture , this is the format of getting the images from Bing images , I would have preffered 
    using Google as the source but their crawler is having some issues so Bing will suffice for now!
    Make sure you populate your dataset in this way and give the max number to set how many pictures you want in your folders
    But keep in mind , you can't straight away scrape 20,000 images of sort because The bing page that you will be searching for has
    a limit ! So go crazy and see what the limit is for scraping !
    
  Now lets connect the datasets and get our model ready for training !
  
  ![alt text](https://github.com/tarun36rocker/Open-contributions/blob/master/pic7.png)
  
    1)train_datagen :: This helps us to create multiple different versions of our data that have because we have only a
    limited dataset . This makes the different versions based on the conditions that we have provided .
    Make sure you enter THE CORRECT DIRECTORY of the folders as seen in the picture above and as instructed before.
    
    2)training_set.class_indices :: helps us check if our model has been successfully connected to the right folders and
    all our categories have been recognised !
    
 Now lets FIT and TRAIN our model on the !
  
  ![alt text](https://github.com/tarun36rocker/Open-contributions/blob/master/pic8.png)
  
    1) fit_generator :: helps us by connecting the test and training data sets and runs the model and helps the model 
    learn between the different categories through multiple epochs(complete run through of data)
    The number of epochs is totally your choice based on your cpu computing power , however be careful while selecting
    because sometimes the more the epochs , your model will start over-fitting which is not good for the 
    performance of your model !
    
    2)save :: We will be saving our model in a .h5 file so that we dont have to wait for hours just to run the program every single time 
    
   Ok! Now lets first test if our model is working by simply sending the picture through a few lines of code as shown below
   
   * The code basically shows that the model is first loaded as seen in LINE 4
   
   * The picture is then loaded and it is converted into an array which is 
   expected by our model for predicting ( as seen in LINES 5-7 )
   
  * LINE 8 recives the prediction from our model
   
   * LINES 9 - 16 is a simple block of code that i wrote which helps us in outputing the category of emotion the model is predicting
   
   ![alt text](https://github.com/tarun36rocker/Open-contributions/blob/master/pic9.png)
   
    This is a picture of me starting at the camera looking quiet emotionless , lets see what our classifier outputs !
   ![alt text](https://github.com/tarun36rocker/Open-contributions/blob/master/pic11.png)
   
   ![alt text](https://github.com/tarun36rocker/Open-contributions/blob/master/pic10.png)
    
    This picutre predicts a list which through coding can be found that it denotes the thrird element which in this case is 
    index 'two' ( considering the array's index starts from 0 } which in terms of our categories means that our model is predicting
    that I am in "Fear"
    Not a bad prediction to be honest !
   Now that we have done a basic check , Lets start by integrating it with the OpenCV to make our model real-time by accessing
   your camera !
   ![alt text](https://github.com/tarun36rocker/Open-contributions/blob/master/pic12.png)
    
   * LINES 1-5 are the set of IMPORTING that is required for the functioning of the code that is about to come
    
   * LINE 6 is required for LOADING the model
    
   * LINE 7 is the line that helps in accessing the webcam at the default port '0' through OpenCV
    
   * LINE 8 is the file that will be used to DETECT OUR FACES in the live frames , this file can easily be downloaded
    from the internet from various sources
    
    Now lets move on to our MAIN FUNCTION that will detect our face from the webcam feed and
    run the frames through the model !
    
   ![alt text](https://github.com/tarun36rocker/Open-contributions/blob/master/pic13.png)
   
   * LINE 14 creates a copy of the frame that is being passed so that the original fame does not get changed or
   corrupted while applying different functions to it
   
   * LINE 15 passes the frame through our HAAR CASCADE filter which finds our face and returns back the coordinates
   of a box which has our location
   
   * LINE 16 -17 go through the coordinates and captures the EXACT region our face is present in 
   
   * LINE 18 RESIZES our frame so as to make it work with our model
   
   * LINE 19 saves every individual frame as a picture so that we can work on them easily rather directly
   taking them as a frame from our webcam
   
   * LINE 20-22 loads our frame ( in the form of a picture ) , converts to an array and makes it suitable
   so as to pass through the model
   
   * LINE 23-29 is a repeat of the function that i have shown above , in short it helps by storing the prediction
   which is the number of the category that the model has predicted 
   
    Now lets move on to add our prediction on the live feed on the opened tab
   
   ![](https://github.com/tarun36rocker/Open-contributions/blob/master/pic14.png)
   
   * The basic IF - ELSE conditions basically figures out which category is mapped to which emotion and also provides
   a colour to them in the BGR colour scheme
   
   * The remaining lines helpes us to write theese predictions on the live webcam feed with the desired colour .
   If you notice we are skipping every next frames (using frame_count) , this is to prevent overlapping of predictions !
   
   * FINALLY we return the image containing the predictions back to the WHILE loop which will be shown next
   
    Lets have a look at the MAIN WHILE LOOP that instigates the whole code
    
  ![](https://github.com/tarun36rocker/Open-contributions/blob/master/pic15.png)
  
  What the while loop basically does is take every frame that it recieves through the webcam and passes it to
  the emotions detection function
  
    Now for the MOST AWAITED MOMENT , LETS FINALLY lets have a look at how the model WORKS!!
    
  ![](https://github.com/tarun36rocker/Open-contributions/blob/master/pic16.png)
  ![](https://github.com/tarun36rocker/Open-contributions/blob/master/pic17.png)
  ![](https://github.com/tarun36rocker/Open-contributions/blob/master/pic18.png)
  
  Looks like computers are able to understand human emotions after all ! 
  Make sure to train your data on more and more images as it yields much BETTER RESULTS !
  
    This is Tarun Krishnan signing off , hope you learnt something from my project !
  
  
    
  
  
    
   
   
   
  
  
    
    
    
    
   
   
   
 
 
    
    
    
    
    
    
    
    
    
   

