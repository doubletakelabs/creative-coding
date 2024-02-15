import py5

number = 5
grow = 0.5
move = 0

def setup():
    global move
    py5.size(800,800)
    move = 0.2

def draw():
    global grow, move
    py5.background(255)
    py5.ellipse(py5.mouse_x, py5.mouse_y, 100 * number, 100 / number)
    py5.rect(py5.mouse_x-50, py5.mouse_y-50, grow, grow)
    grow = grow + .2

    py5.rect(move, 400, 100, 100)
    move = move + 0.2

py5.run_sketch()