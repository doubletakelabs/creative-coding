import py5

def setup():
    py5.size(500,500)
    
def draw():
    x = 0
    while x < py5.width:
        py5.line(x, 0, x, py5.height)
        x += 50

    y = 0
    while y < py5.height:
        py5.line(0, y, py5.width, y)
        y += 50

py5.run_sketch()