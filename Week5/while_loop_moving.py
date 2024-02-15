import py5

y = 0

def setup():
    py5.size(500,500)
    
def draw():
    global y
    py5.background(0) # sets the background to black
    x = 0
    while x <= py5.width:
        py5.ellipse(x, y, 50, 50)
        x = x + 50 
    y = y + 1

    if y >= py5.height+50: # if the circle goes below the height of the canvas + 50 pixels, go back to the top
        y = -50
    
    print(y)

py5.run_sketch()