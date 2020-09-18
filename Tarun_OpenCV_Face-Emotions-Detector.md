# **Face Emotions Detector**
    by Tarun Krishnan
 Follow me on
   * Linkedin : https://www.linkedin.com/in/tarunkrishnan2000/
   * Github : https://github.com/tarun36rocker?tab=repositories
   -------------------------------------------------------------
 Now on to This Amazing and Simple Project that I made !
      
    The Main Aim was to try to understand if a computer can understand human emotions . Think about it this way ,
    computers are REALLY smart when it comes to crunching down numbers or even trying to find correlations in 
    datasets that they have never seen before in just a few minutes or hours! Something which humans study their whole lives for !
    So that really was the purpose of this project , to see if just by providing few images if a computer
    can understand basic human emotions , something which even humans find difficult to understand !
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
    that there are 3 subfolders - 1)single_pred - which will be used to check if the model is working after compiling the model
    2) test_set - folder used to contain the test data 3) training_data - folder used to contain the training data
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
    
  Now lets TRAIN our data !
  
  ![alt text](https://github.com/tarun36rocker/Open-contributions/blob/master/pic7.png)
    
    1)train_datagen :: This helps us to create multiple different versions of our data that have because we have only a
    limited dataset . This makes the different versions based on the conditions that we have provided .
    Make sure you enter THE CORRECT DIRECTORY of the folders as seen in the picture above and as instructed before.
    
    2)training_set.class_indices :: helps us check if our model has been successfully connected to the right folders and
    all our categories have been recognised !
    
    
    
    
   
   
   
 
 
    
    
    
    
    
    
    
    
    
   

