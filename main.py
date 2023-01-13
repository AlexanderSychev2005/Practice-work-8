import pgzrun
import pygame

from pgzero.actor import Actor

WIDTH = 600
HEIGHT = 700
RED = 200, 0, 0
Darkviolet = 104, 34, 139
# Paddle = Rect((20, 100), (100, 10))
# Ball = Rect((5, 200), (100, 5))


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add(self, other):
        return Vector(self.x + other.x, 0)

    def __sub__(self, other):
        return Vector(self.x - other.x, 0)


class Paddle:
    def __init__(self, l, h, s1, s2):
        self.position = l, h
        self.size = s1, s2
        self.rect = Rect(self.position, self.size)


my_paddle = Paddle(200, 600, 100, 20)


class Ball:
    def __init__(self, x, y):
        self.position = Vector(x, y)

    def draw(self):
        screen.draw.filled_circle((self.position.x, self.position.y), 13, "darkviolet")

    def update(self):
        pass


ball = Ball(300, 300)



def draw():
    screen.clear()
    screen.draw.rect(my_paddle.rect, RED)
    ball.draw()


def on_mouse_move(pos):
    x = pos[0]
    my_paddle.rect.centerx = x


def update(dt):
    ball.position.y += 2
    pass


pgzrun.go()
