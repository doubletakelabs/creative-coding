import py5

def setup():
    py5.size(700,700)
    
def draw():
    py5.background(0) # sets the background to black
    x = 0
    while x < py5.width:
        # check if the mouse position is within a 30 x 30 boundary, based on the position of the circle that will be drawn
        if py5.mouse_x > x - 15 and py5.mouse_x < x + 15 and py5.mouse_y > py5.height/2 - 15 and py5.mouse_y < py5.height/2 + 15:
            py5.fill(30,200,200) # change the fill if the mouse is within the boundary
        else:
            py5.fill(255) # otherwise make the fill white

        py5.ellipse(x, py5.height / 2, 30, 30) # draw the circle at that location
        x = x + 30 # increment x by 30 and draw another circle across the canvas

py5.run_sketch()