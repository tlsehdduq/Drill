import sys
import random
import game_framework
from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:

    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(200, 580)
        self.frame = 0
        self.image = load_image('bird100x100x14.png')
        self.velocity = 0
        self.dir = 1



    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

team = [Boy() for i in range(5)]

grass = Grass()

running = True

while running:
    handle_events()

    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()

    update_canvas()

close_canvas()
