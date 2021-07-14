// A Hello World Applet
// Save file as HelloWorld.java
  
import java.applet.Applet;
import java.awt.Graphics;
  
/*
<applet code="HelloWorld" width=200 height=60>
</applet>
*/
  
// HelloWorld class extends Applet
public class HelloWorld extends Applet 
{
    // Overriding paint() method
    @Override
    public void paint(Graphics g) 
    {
        g.drawString("Hello World", 20, 20);
    }
      
}
# run "appletviewer HelloWorld" in cmd