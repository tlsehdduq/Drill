from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90

z=270

while True:

    while x <750:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x+=2
        delay(0.01)

    while y<550:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y+=2
        delay(0.01)

    while x>30:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x-=2
        delay(0.01)
        
    while y>90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y-=2
        delay(0.01)
    while x <=400:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x+=2
        delay(0.01)

 

    while z>-90:
        
        x=210*math.cos(z/360*2*math.pi)+400
        
        y=210*math.sin(z/360*2*math.pi)+300
        
        clear_canvas_now()
        
        grass.draw_now(400,30)
        
        character.draw_now(x,y)
        
        z-=1
        
        delay(0.01)

   



close_canvas()
