<h1 align="center">Face Detection Using OpenCV</h1>   
<p align="center">Face Detection System. Here were used OpenCv modules and HaasarCodes to identify the face from an camera feed. Deployed it using Flask, here we didn't focus on the browser look and feel(html,css) part, as the main aim is to detect the face.</p>

**Want to try**
-  Clone the repository `git clone https://github.com/AdicherlaVenkataSai/Open-contributions.git`
-  Get into the directory where the code is available. `cd VenkataSai_OpenCV/"1. Face Detection"`
-  Now your at the location, run the program `python main.py`
-  You can find output like `Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
-  Copy paste the link over the browser and hit run.  Cheers!!! 

**Approach:**     
1. First let's install all the required modules like,
-  opencv : `pip install opencv-python`
-  numpy  : `pip install numpy`
-  flask  : `pip install Flask`
2. Let's get the `hassercodes` which are helpful to detect the faces.
3. Now lets develop a `camera.py` function, which helps us capturing the faces from the live feed camera.
```python
import cv2
import numpy as np
import requests

class VideoCamera(object):
    def __init__(self):

        self.video = cv2.VideoCapture(0)

    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        success, image = self.video.read()
        image = cv2.flip(image,180)
        faces = face_cascade.detectMultiScale(image, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
            roi_color = image[y:y+h, x:x+w]
        ret, jpeg = cv2.imencode('.jpg', image)

        return jpeg.tobytes()

```
4. As were deploying it on local browser using `flask`, so this is the flask code.
```python
from flask import Flask, render_template, Response
from camera import VideoCamera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug = True)

```
5. At last we need to make a `html` to host the flask application on local machine.
```
<html>
  <head>
    <title>Face Detection</title>
  </head>
  <body>
    <h1>Face Detection Using OpenCV</h1>
    <img id="bg" src="{{ url_for('video_feed') }}">
  </body>
</html>
```
**Note: Were not much focusing on the look and feel part of browser**


Here the demo:    
**Don't mind the quality(compressed to fit)**

![testing111-min](https://user-images.githubusercontent.com/26376075/93674954-68181280-fac9-11ea-9334-bc0765f2389c.gif)
