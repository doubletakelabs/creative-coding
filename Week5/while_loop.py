import py5

def setup():
    py5.size(500,500)
    # the rect_mode(CENTER) below changes the rect() command to interpret the first two parameters as the rectangle's center point 
    # and the third and fourth parameters to be the width and height
    py5.rect_mode(py5.CENTER) 


def draw():
   x = py5.width
   while x >= 0:
      py5.rect(py5.width/2, py5.height/2, x, x)
      x = x - 50 

py5.run_sketch()