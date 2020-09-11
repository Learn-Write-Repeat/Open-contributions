# Draw geometric shapes and write text on images using OpenCV

The basic operations of OpenCV is to draw over images. The ability to add different geometric shapes just like lines, circles and rectangle etc.
<p>OpenCV provides many drawing functions to draw geometric shapes and write text on images. some of the drawing and text writing functions are listed below.</p>


<section>
<b>cv2.line() :</b> This function is used to draw line on an image.<br>
<b>cv2.arrowedLine():</b> This function is used to draw arrowed-line on image<br>
<b>cv2.rectangle() :</b> This function is used to draw rectangle on an image.<br>
<b>cv2.circle() :</b> This function is used to draw circle on an image.<br>
<b>cv2.ellipse() :</b> This function is used to draw ellipse on image.<br>
<b>cv2.polylines() :</b> This function is used to draw polygon on image.<br>
<b>cv2.putText() :</b> This function is used to write text on image.<br>
</section>


<section class="main">
Now let's see the attributes of each function in order to use it.
</section>

## **1) cv2.line()**

    cv2.line(img, (pt1, pt2), (pt3, pt4), color, thickness)

 #### Parameters:
    img – Image.
    pt1, pt2 – Starting point(x1,y1) of the line segment.
    pt3, pt4 – Ending point(x2,y2) of the line segment.
    color – Line color in BGR mode.
    thickness – Line thickness.
    
#### Figure 1. Parameters of Line :

<img style= "border:1px solid black" src="SharedScreenshot.jpg">

<br>
<br>
<br>

## **2) cv2.arrowedLine()**

    cv2.arrowedline(img, (pt1, pt2), (pt3, pt4), color, thickness)

 #### Parameters:
    img – Image.
    pt1, pt2 – Starting point(x1,y1) of the line segment.
    pt3, pt4 – Ending point(x2,y2) of the line segment.
    color – Line color in BGR mode.
    thickness – Line thickness.
    
#### Figure 2. Parameters of Arrowedline :

<img style= "border:1px solid black" src="arrow.jpg">

## **3) cv2.rectangle()**

    cv2.rectangle(img, (pt1, pt2), (pt3, pt4), color, thickness)

 #### Parameters:
    img – Image.
    pt1, pt2 – Top left corner point(x1,y1) of the rectangle.
    pt3, pt4 – Bottom right corner point(x2,y2) of the rectangle.
    color – Rectangle color in BGR mode.
    thickness – Rectangle thickness.
    (if the thickness = -1 then we get a filled rectangle)
    
#### Figure 3. Parameters of Rectangle :

<img style= "border:1px solid black" src="rect2.jpg">


## **4) cv2.circle()**

    cv2.circle(img, (pt1, pt2), radius, color, thickness)

 #### Parameters:
    img – Image.
    pt1, pt2 – Center coordinates if the circle.
    radius - Radius of the circle
    color – Circle color in BGR mode.
    thickness – Circle thickness.
    (if the thickness = -1 then we get a filled circle)
    
#### Figure 4. Parameters of Circle :

<img style= "border:1px solid black" src="circle2.jpg">


## **5) cv2.polylines()**

    cv2.polylines(img, array, true/false, color, thickness)

 #### Parameters:
    img – Image.
    array – The array of coordinates
    true/false – True, if it is a closed line
    color – Color of the stroke.
    thickness – Stroke thickness.
    (if the thickness = -1 then we get a filled polygon)
#### Figure 5. Parameters of Polygon :

<img style= "border:1px solid black" src="poly2.jpg">


## **6) cv2.ellipse()**

    cv2.putText(img, (pt1, pt2), (h, w), r_angle, s_angle, f_angle, color, thickness)

 #### Parameters:
    img – Image.
    pt1, pt2 – Center Coordinates of the ellipse.
    h, w – Length of the minor and major axes
    r_angle - Rotation angle of the ellipse (calculated clockwise)
    s_angle - Starting angle (calculated clockwise)
    f_angle - Final angle (calculated clockwise)
    color – Color of the text.
    thickness – Text thickness.
    (if the thickness = -1 then we get a filled ellipse)
    
#### Figure 6. Parameters of Ellipse :

<img style= "border:1px solid black" src="ell.png">


## **7) cv2.putText()**

    cv2.putText(img, (pt1, pt2), font_style, size, color, thickness, line_style)

 #### Parameters:
    img – Image.
    pt1, pt2 – Starting point of the text.
    font_style – Style of the font.
    color – Color of the text.
    thickness – Text thickness.
    line_style – Line style of the font.
    
#### Figure 7. Parameters of Text :

<img style= "border:1px solid black" src="text.jpg" height=300px width=500px>

<br>
<br>

## Why to draw shapes and write text on images :

- Writing text on image used to describe the image.
- By using gemetrical shapes we can highlight any particular area in the image.
- Geometrical shapes like line helps us to specify some object in the image.

        






