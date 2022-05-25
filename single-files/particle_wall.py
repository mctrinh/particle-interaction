import pygame as pg, sys
from pygame.locals import *
from random import randint
import math

W = 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

particle_num = int(input('Enter the number of particles you want: '))

class Particle:
    def __init__(self, dx, dy, x, y, radius, color):
        self.dx = dx
        self.dy = dy
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.min_radius = radius

    def draw(self):
        pg.draw.circle(s, self.color, (self.x, self.y), self.radius)

def color_generator(): return [randint(100, 255) for _ in range(3)]     # _ are the throughaway variables, aren't actually used

particle_list = []
for i in range(particle_num): particle_list.append(Particle(randint(1, 3), randint(1, 3), randint(10, W), randint(10, W), randint(1, 10), color_generator()))

def animate():
    mx = pg.mouse.get_pos()[0]
    my = pg.mouse.get_pos()[1]
    for p in particle_list:
        p.draw()
        if p.x > W or p.x < 0: p.dx = -p.dx
        if p.y > W or p.y < 0: p.dy = -p.dy
        p.x += p.dx
        p.y += p.dy

        if math.fabs(mx - p.x) < 50 and math.fabs(my - p.y) < 50 and p.radius < 200: p.radius += 1
        elif p.radius > p.min_radius: p.radius -= 0.5

#s = pg.display.set_mode((0, 0))            # same size as screen resolution, can use one '0'
#s = pg.display.set_mode((1920, 1080))      # can also specify manually
s = pg.display.set_mode((W, W))             # return a surface 's'
clock = pg.time.Clock()

while True:
    s.fill(WHITE)                           # 'fill' called within 'surface' module, not in 'set_mode' module
    animate()
    for e in pg.event.get():                # each 'e' is a list
        if e.type == QUIT:
            pg.quit()
            sys.exit()

    clock.tick(80)                          # update the clock, called each frame, max=80 fps
    pg.display.update()
    