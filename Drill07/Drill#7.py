from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def motion():
    global a_x, a_y, x, y
    if a_x > x:
       x += 1
    elif a_x < x:
       x -= 1
    elif a_y > y:
       y += 1
    elif a_y < y:
       y -= 1
    if(a_x, a_y) == (x, y):
       a_x, a_y = random.randint(1, KPU_WIDTH), random.randint(1, KPU_HEIGHT)

    delay(0.01)

# def handle_events():
#     global running
#     global x, y
#     global ax, ay
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             running = False
#         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#             running = False
#
#     pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)


kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
a_x, a_y = random.randint(1, KPU_WIDTH), random.randint(1, KPU_HEIGHT)
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    hand_arrow.draw(a_x, a_y)
    motion()
    update_canvas()
    frame = (frame + 1) % 8

    # handle_events()

close_canvas()