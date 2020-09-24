# Natural Language Processing

**Before we dive deep into the concept of Word Embedding,it is important to have a basic idea of Natural Language Processing. So lets have a small introduction,shall we?**

 - [ ] ***In simple words,NLP is how computers perceive and analyze the languages,which we use to communicate with each other***
 
 ![Language Communication](https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_892,h_550/https://www.tridindia.com/wp-content/uploads/2019/05/major-Difference-Between-Language-And-Communication-892x550.jpg)
 
  - [ ] *It has tons of applications ,from Amazon Alexa that we use in our homes to the Swiggy chatbots that we talk to while tracking our ordered food!*
# Word Embeddings 
### **Now that we know what NLP is,let's learn about an interesting way of representing different words:**

 - [ ] ***Word embeddings** is nothing but representation of words in the form of vectors **where words having similar meaning point to the same direction***
 - [ ] *For example,the vectors of the words such as important,essential and crucial may point in the same direction as they have similar meanings,so they are grouped together*
 
 ![Embedding projector 1](https://2.bp.blogspot.com/-Uql7bl2KEYM/WEfQ4Kl_0YI/AAAAAAAABck/GkktuPM8KoMcMl2Tot6GzH3-NgwPNETMgCLcB/s1600/image03.png)
 
  - [ ] *Looks interesting ,but how does it happen?*
     - *Let's understand the procedure through an interesting project which I did last month,using a dataset called ''IMDB Reviews''*
     - ***This dataset basically contains thousands of sentences of reviews(called features)** of different movies on the IMDB website given by different people ,and **along with type of the corresponding review ,0 for bad and 1 for a good review (called labels)***
     - *This data was fed into a neural network(Deep Learning),in order to  analyze the words in these sentences which corresponds to the type of review ,i.e,positive or negative*
     - ***After the model was done training on the data,it could predict on never seen text(review) given by us ,whether it is a negative or a positive one!***
    
    ![Embedding Projector 2](https://miro.medium.com/max/990/1*Fat62b1ZITOFMPXTcHNkLw.jpeg)
    
    * As shown above,**using an embedding projector(which is easily available online),we can view the projections of these words,where similar words are grouped together**!Looks cool,doesn't it?

 - [ ]  The datasets used may vary ,as it may be used for a different application**,say Sarcasm Detection,but the concept pretty much reamins the same*. 


### *Now that we have understood the concept of Word Embeddings ,lets do some coding to implement it!*
