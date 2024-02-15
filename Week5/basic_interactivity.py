import py5

def setup():    
    py5.size(500,500)

def draw():
    if py5.is_mouse_pressed: # is mouse is pressed
        py5.background(150,0,150) # set the new background color
        py5.text_size(50) # set the text size
        py5.text("Wow!", 200, 250) # print the text
    else:
        if py5.mouse_x > 250: # if mouse is on right side of the canvas
            py5.background(200,200,200) # set the background color
        else: # if mouse is on the left side of the canvas
            py5.background(0,125,67) # set the background color
        py5.line(py5.mouse_x, py5.mouse_y, 400, 400) # draw a line using the x,y coordinate of the mouse as the starting point

py5.run_sketch()
