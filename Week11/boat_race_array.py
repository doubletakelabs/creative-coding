import py5
import random

class Boat:
    def __init__(self, teamName="", color=0, x=0, y=0, speed=0):
        self.teamName = teamName
        self.color = color
        self.xpos = x
        self.ypos = y
        self.speed = speed
        self.lapCount = 0
    
    def display(self):
        py5.fill(255)
        py5.rect(self.xpos, self.ypos, 100, 10)
        py5.rect(self.xpos, self.ypos-30, 10, 80)
        py5.arc(self.xpos, self.ypos+5, 100, 50, 0, py5.PI, py5.OPEN)
        py5.fill(self.color)
        py5.triangle(self.xpos, self.ypos-70, self.xpos-40, self.ypos-40, self.xpos, self.ypos-20)

    def move(self):
        self.xpos += self.speed
        if (self.xpos > py5.width + 50):
            self.ypos = random.randint(100, 500)
            self.xpos = -50
            self.speed = random.randint(1,8)
            self.lapCount += 1
            print(f"{self.teamName} is on lap #{self.lapCount}")
        
boats = [Boat(f"Team {i+1}", py5.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), random.randint(0, py5.width), random.randint(100, 500), random.randint(1, 8)) for i in range(30)]

def setup():
    py5.size(500, 500)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.background(125)
    for boat in boats:
        boat.move()
        boat.display()

py5.run_sketch()