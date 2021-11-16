import game_framework
from pico2d import *
import game_world
import random

# 참새의 평균 비행 속도 29~40km 따라서 참새로 가정하고 속도를 20키로로 설정해주었고
# 참새의 크기 20cm 20cm로 설정
# 사람 기준 74pixel boy = 10 pixel 30 cm 총 2.2m
# 전체 74pixel일때 20 cm

PIXEL_PER_METER = ( 7.4/ 2.0 )  # 전체 74pixel일때 20 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Birds:

    def __init__(self):
        self.x, self.y = random.randint(20, 900),random.randint(200,600)
        self.image = load_image('bird100x100x14.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0

    def get_bb(self):
        # fill here
        return 0, 0, 0, 0

    def update(self):

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        if self.dir == 1:
            self.x += RUN_SPEED_PPS
            if self.x >= 1200:
                self.x -= RUN_SPEED_PPS
                self.dir = 0
        if self.dir == 0:
            self.x -= RUN_SPEED_PPS
            if self.x <= 50:
                self.x += RUN_SPEED_PPS
                self.dir = 1

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
