<h1>Cascade Classifiers</h1>
<h2>What are cascade classifiers ?</h2>
<p>Cascading classifiers are trained with several hundred "positive" sample views of a particular object and arbitrary "negative" images of the same size. ... After the classifier is trained it can be applied to a region of an image and detect the object in question.</p>
<h2>Origins</h2>
<p>So basically this approach of calssifying things was introduced by Paul Viola and Michael Jones in their paper Rapid Object Detection using a Boosted Cascade of Simple Features. So it is a machine learning based approach where a lot of positive images(images that we want our classifier to classify) and negative images were trained in order to create cascade classifier.</p>
<h3>How to make your own cascade classifier ?</h3>
<p>Train Dataset to XML file for Cascade Classifier OpenCV</p>
<ol>
  <li>find your positive image and put in the positive folder.</li>
  <li>find your negative image and put in the negative folder.</li>
   <li>create name list of positive image and negative image</li>
   <li>create file samples .vec of positive image by use createsamples.pl. </li>
    <li>run script merge file samples .vec by use mergevec.py. </li>
  <li>Start training.</li>
  </ol>
  
  
  
  <h2>Application of Cascade Classifier</h2>
  <p>Cascading classifiers are trained with several hundred "positive" sample views of a particular object and arbitrary "negative" images of the same size.It can be used to detect a lot of features in images or in a love video like faces, facial features, hand recognition and as you can create your own classifiers also, there is no limit to them. .</p>
