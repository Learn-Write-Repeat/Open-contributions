# How to approach a Machine Learning problem ??

This page discusses a *generic step-wise approach* on attempting to solve a problem at hand using Machine Learning. However in real practice, not all steps would be 
necessarily taken depending on the problem statement, time constraints, computation power/tools available, the data and the final goal. But these steps would provide a 
good mind-map to a beginner or intermediate ML practitioner so as to understand how all the ML concepts fit together in the puzzle, when each concept needs to be applied
and to not forget or skip any necessary element along the way.

I would first list out the approach taken by a newbie in ML (which is not wrong or incorrect given the early stage) and then discuss what changes and additions need 
to be made in his approach as he transitions ahead in his ML journey. 

So lets get started...

## How would a beginner face an ML problem?
  - Fetch the dataset from an open source (mostly a well defined excel/csv sheet)
  - Take a quick look at the dataset and perform basic cleaning and arranging of data
  - Assigning the feature and target variable according to the problem statement
  - Try out one or two ML algorithms by looking at the output variable datatype and build their models
  - Compare model accuracy on test data
  - Pick out the model which gives best accuracy
  - FINISH
  
If only it would have been that easy! Although happy today, sooner or later the beginner would realize the above listed steps dont just go well with one another in sequence. 
The data he gets is messy, the problem statement doesn't seem to be clear when taking a look at the data, there would be many ML algorithms that would seem suitable 
for use, the accuracy score doesn't tally when the model is put to practice or the created model does not give results upon which the next steps can be taken upon.

Thats when the current known mini-approach needs to undergo some mature changes

## Generic and recommended approach to deal with an ML problem:

  - **Understand thoroughly the Problem Statement - Do you really need ML?**
  
    This may sound vague, but many simple business problem statements that can be well solved using traditional methods or basic data reporting are fed into computationally 
    expensive ML models, wasting time and resources. Being an ML Engineer is of no real use when you can't figure out if the business problems really require Machine Learning
    Algorithms. From a business approach, cost efficiency and flexibility of the proposed solution should be the sole motive when building solutions.
    This requires a very deep and clear-cut understanding of the business problem statement. Here aresome points that need to be thought of:
      - What is the main goal/motive that needs to get fulfilled?
      - Is the problem statement straightforward or ambiguous?
      - Can the problem be solved by traditional methods, basic data analytics/reporting or simply by pure expertise consultation?
      - Is the same problem occuring again and again?
      - What are the next steps that need to be taken after acquiring the problem solution?
      - What is the impact of the problem statement and to who will it prove beneficial?
      
     After getting the above answers, you will surely know if Machine Learning is the right boat to hop into for your problem statement.
     
  - **Gather the RIGHT data**
  
     After deeply understanding the purpose, depth and scope of the problem, the very next step is to fetch or look out for the *right* data that will suit your business 
     needs and is relevant enough to gain insights. The domain experts should be consulted, available resources should be listed and discussed upon and if additional
     data is needed should be again searched. The most important aspect to keep in mind is that RIGHT data should be collected. Here are some of the points when looking 
     out for the RIGHT data:
     
       - Is the data relevant to my business use case?
       - Does the data cover the important dimensions and factors that will impact my solution output?
       - Is the data not too complicated to understand and not very costly?
       - Is the data accurate? Does it has any hidden assumptions or constraints?
       - Does the data cover all target category instances or only a subset of them?
         (eg. for understanding the health habits of the entire US population, only gathering data related to the US youth would not be sufficient)
       - Is the data in a sufficient quantity?
       - Does the data comply with user privacy and/or business security agreements?
       
     This process is expected to take ample time since the correct data should be collected. However for building a rough/prototype solution, don't spend 
     ages for the process since the process can also be re-iterated upon once the solution version is accepted for further builds and improvements.
     We then move on to the next step.
     
     
  - **Data Exploration**
    
      This step indicates a quick data exploration activity that you do to get familiar with the dataset. This step is NOT related to Exploratory Data Analysis where we 
      try to validate some assumptions we must have made to gain deep insights for maing decisions. This is just a basic glimpse that to take into your data window and 
      figure out what treatments are to be made later.
      
       - Plot few basic charts like bar chart , box-plot and histogram
       - See some descriptive statistics of the data
       - Get a gist of what to do next keeping your problem statement in mind
  
  - **Select an ML Algorithm**
  
     Now that you have gained the knowledge of your dataset's basic characteristics, its time to list down a few ML Algorithms that may help in solving the problem.
     This depends highly on the target variable, type of learning and features available.
       
       ![](https://blogs.sas.com/content/subconsciousmusings/files/2017/04/machine-learning-cheet-sheet.png)
       
     There are many more models to choose from:
     
       ![](https://s3.amazonaws.com/MLMastery/MachineLearningAlgorithms.png?__s=skh1zniyiw9vuz7ppzxp)
       
       
  - **CLEAN and PREPARE and REDO!!**
  
     About 75% to 80% of time of a Data Scientist/ML Engineer goes into cleaning the real world messy data and preparing it so that it can be consumed by the models.
     Different ML algorithms need different preparation and cleaning of data. \
     
     Here is a basic list to get started with: (however not all may be required depending on your use case)
     
       ![](https://media.geeksforgeeks.org/wp-content/uploads/20190312184006/Data-Preprocessing.png)
       
  - **Run and Evaluate your model**
  
     Very straightforward - create,run and test your model on the testing data. Keep in mind that there are tons of evaluation criteria to compare which model is the best of 
     all apart from accuracy metrics. Select your model by choosing your eveluation metrics wisely.
     Here area few basic metrics to explore:
     
     ![](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2019/12/How-to-Choose-a-Metric-for-Imbalanced-Classification-latest.png)
      
  -  **Tweak the chosen model**
  
      After you finally select a good model for your problem statement, tweak its hyperparameters to polish it for the real world data. Check if its output matches
      your business problem expectations.
      
  - **Consume the results**
  
      This part is often neglected by most of the ML Engineers, how to effectively present/deploy the model for the client. Some aspects include:
      
       - Present your findings in a documented format
       - Deploy the model to run at scale
       - Storytelling your ML Process to your business stakeholders
        
  - **FINISH, Yet Starting**
  
       With this we may have finished with the Problem Solving Approach, but ML engineers have a lot to yet in real world. This includes real time deployment or CI/CD
       of the model, making it scalable, health checking of the data and the model and much more. While we dont cover those advanced concepts, it is recommended
       that you learn about it at your later stages.
       
Here is an awsome reference for everyone who wants to go in depth or learn each of the steps mentioned above from scratch.  
https://machinelearningmastery.com/start-here/
    
    
Written By:
Inziya Dossa   
https://www.linkedin.com/in/inziya-dossa/
    
    
