import py5
from playsound import playsound

def setup():
    py5.size(500,500)
    
def draw():
    if py5.is_key_pressed:
        if py5.key in [' ']:
            playsound('ArcadeRetroGameOver.wav')

py5.run_sketch()