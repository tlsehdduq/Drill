from pico2d import *
import random
# Game object class here

class Grass:
    def __init__(self): #생성자
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


# Grass 라는 클래스로부터 , grass객체를 생성한다.
class Boy: #클래스를 만들었으면객체를 생성
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)

    def update(self): #소년의 행위 구현
        self.x += 5 # 속성값을 바꿈으로 써 행위를 구현
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class dropBall:

    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(100, 700), 599


    def update(self):
        self.y -= random.randint(10,50)
        if self.y <= 60:
            self.y = 60
    def draw(self):
        self.image.draw(self.x, self.y)

class dropBigBall:

    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(100, 700), 599


    def update(self):
        self.y -= random.randint(10,50)
        if self.y <= 60:
            self.y = 60

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():

    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code initialization 여러가지 객체를 다 만든다.
#그 다음에는 여러가지 상호작용을 시뮬레이션. Game Logic
#Drawing 그결과를 보여줌 Rendering이라고도 부름

open_canvas()

grass = Grass()#잔디 객체를 생성
# boy = Boy()
#python list comprehension
#리스트를 빠르게 만들기 위한 독특한 문법 구조
#리스트 안에 있는 데이터들을 일정한 규칙을 가지고 생성해냄
#team

team = [Boy() for i in range(11)]

Ball = [dropBall() for i in range(20)]

BigBall = [dropBigBall() for i in range(20)]

running = True
# game main loop code
while running:
    handle_events() #키를 받아들이는 자리

    #game logic
    for boy in team:
        boy.update()

    for balls in Ball:
        balls.update()

    for bigballs in BigBall:
        bigballs.update()
    #game drawing
    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()

    for balls in Ball:
        balls.draw()

    for bigballs in BigBall:
        bigballs.draw()

    update_canvas()

    delay(0.05)

    update_canvas()

# finalization code