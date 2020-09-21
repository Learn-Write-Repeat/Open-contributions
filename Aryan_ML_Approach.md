# Census Income Prediction

## About me:book::
I am a computer science student with interest in problem solving and automating things using python, machine learning and other technologies.

Reach me at :email::
* Github: https://github.com/AryanRastogi7767
* Gmail: aryanrastogi97@gmail.com
* Linkedin:  https://www.linkedin.com/in/aryan-rastogi-b38ba1190/

**In this Markdown file I will describe the approach to the problem of Census Income Prediction. Below are some details about the dataset. The dataset can be downloaded easily from kaggle or from the UCI ML repository website. Contact me in case of any doubts or queries. See my Github for similar projects.**

**Dataset:** Census Income Data from UCI Machine Learning Repository

**Task:** Predict whether income exceeds 50K/yr based on census data. (Binary Classification)

**Data Set Information:**

Extraction was done by Barry Becker from the 1994 Census database. A set of reasonably clean records was extracted using the following conditions: ((AAGE>16) && (AGI>100) && (AFNLWGT>1)&& (HRSWK>0).

### Attribute information:
**Listing of attributes:**

* **salary:** >50K, <=50K.
* **age:** continuous.
* **workclass:** Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
* **fnlwgt:** continuous.
* **education:** Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st- 4th, 10th, Doctorate, 5th-6th, Preschool.
* **education-num:** continuous.
* **marital-status:** Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF- spouse.
* **occupation:** Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed- Forces.
* **relationship:** Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
* **race:** White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
* **sex:** Female, Male.
* **capital-gain:** continuous.
* **capital-loss:** continuous.
* **hours-per-week:** continuous.
* **native-country:** United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand- Netherlands.

### More info on the Data
**Number of Instances**
* 48842 instances, mix of continuous and discrete (train=32561, test=16281)
* 45222 if instances with unknown values are removed (train=30162, test=15060)
* Split into train-test using MLC++ GenCVFiles (2/3, 1/3 random).

**Number of Attributes**
* 6 continuous, 8 nominal attributes.

**Missing Attribute Values:**
* 7% have missing values.

**Class Distribution:**
* Probability for the label '>50K' : 23.93% / 24.78% (without unknowns)
* Probability for the label '<=50K' : 76.07% / 75.22% (without unknowns)

## Approach To  The Problem:

* Import Necessary Libraries
* Import Data into DataFrames
  - The dataset was already split into training and testing data so the training data was imported first.
*  Checking and analysing the information on the training data using *.info() and .describe()* methods.
* Exploratory Data Analysis and Feature Engineering:
  - Checking if the dataset is balanced or imbalanced.
  - Handling the null values.
  - Label Encoding Categorical Variables.
  - Checking Correlation between features.
  -Checking correlation between features and target variable.
  - Removing Highly Correlated Columns. Eg, Sex and Relationship, Education and Education_num.
  - Performaing Data Analysis on Features to understand the relationships between them.
  - Data Visualizations
* Data Preparation
  - Convert age column to Categorical.
  - Perform analysis individually on different features and prepare them accordingly.
  - Generealize categories in the occupation ,marital status and native country column to reduce the number of features in the end.
* Remove Features that are not useful to our analysis.
* One Hot Encode the Categorical Features to form new features
* Remove Highly Correlated Features.
* Standardize the data.
* Split the training data into training and validation.
* Train the ML Models and test them on the validation data . 
  - Save and analyse the results.
  - Perform Hyperparameter tuning on the best classifier to make it better.
* Perform Upsampling of the data.
  - Train the ML Models
  - Save and analyse the results
  - Perform hyperparameter tuning on the best classifier to make it better.
* Import the test data.
* Perform the same data preprocessing steps on the test data.
* Test the classifers with best performance on the  test data.
* Analyse the results.
* Save and Deploy the model that works best on the classification task.
  







