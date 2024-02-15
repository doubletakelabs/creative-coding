# this code is slightly modified from the "drawing basic elements" page of the py5coding.org website
#https://py5coding.org/tutorials/intro_to_py5_and_python_02_drawing_2d_primitives.html

import py5

def setup():    
    py5.size(500,500)

def draw():
    #dark blue background
    py5.background("#004477")

    py5.stroke(255,255,255)
    py5.stroke_weight(3)

    #red rectangles
    py5.fill(255,0,0)
    py5.rect(100, 150, 200, 300)
    py5.rect(10,15, 20,30)

    #orange rectangle
    py5.fill(255,153,0)
    py5.rect(50,100, 150,150)

    # fill-less square
    py5.no_fill()
    py5.rect(250,100, 150,150)

py5.run_sketch()