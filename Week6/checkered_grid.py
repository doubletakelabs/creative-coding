import py5

grid = 8
squareSize = 0

def setup():
    global squareSize
    py5.size(600,600)
    squareSize = py5.width/grid
    
def draw():
    w = 0
    h = 0
    while w < py5.width:
        while h < py5.height:
            if (h+w) % 2 == 0:
                py5.fill(255)
            else:
                py5.fill(0)
            py5.rect(h, w, squareSize, squareSize)
            h += squareSize
        w += squareSize
        h = 0

py5.run_sketch()
