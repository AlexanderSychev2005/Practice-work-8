import time
import sys
import pgzrun
import pygame

from pgzero.actor import Actor


WIDTH = 600
HEIGHT = 700
RED = 200, 0, 0
Darkviolet = 104, 34, 139
COLOR1 = 71,60,139
WHITE = (255, 255, 255)
BOX = Rect((20, 100), (100,10))
RADIUS = 13
ball_speed_x = -3
ball_speed_y = 3
hearts = [Actor("heart", (20, 20)), Actor("heart", (55, 20)), Actor("heart", (90, 20))]
score =0

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
        self.position = [l, h]
        self.size = s1, s2

    def draw(self):
        screen.draw.filled_rect(Rect(self.position, self.size), RED)


my_paddle = Paddle(200, 600, 100, 20)


class Rectangle:
    def __init__(self,x, y, w, h):
        self.x = x
        self.y = y
        self.h = h
        self.w = w

    def draw(self):
        rect = Rect(self.x, self.y, self.h, self.w)
        screen.draw.filled_rect(rect, "blue")


rectangles = []
rectan_count = 0
x = 30
y = 50
while rectan_count < 18:
    rectangles.append(Rectangle(x, y, 20, 50))
    rectan_count += 1
    x += 80
    if rectan_count == 7:
        y += 30
        x = 70
    elif rectan_count == 13:
        y += 30
        x = 110


class Ball:
    def __init__(self, x, y):
        self.position = Vector(x, y)

    def draw(self):
        screen.draw.filled_circle((self.position.x, self.position.y), RADIUS, "darkviolet")

    def update(self):
        pass


ball = Ball(300, 300)



def draw():

    global ball_speed_x, ball_speed_y, score
    screen.clear()
    my_paddle.draw()
    ball.draw()

    if hearts:
        for heart in hearts:
            heart.draw()

    else:
        screen.clear()
        screen.draw.text("Sorry, you lose!!", (150, 200), color="blue", fontsize=50)

    if rectangles:
        for rectangle in rectangles:
            if (rectangle.x <= ball.position.x <= (rectangle.x + rectangle.w)) and (rectangle.y <= ball.position.y <= (rectangle.y + rectangle.h)):
                ball_speed_y *= -1
                rectangles.remove(rectangle)
                score += 1
            rectangle.draw()

        screen.draw.text("Score:" + str(score ), (30, 30), color="blue", fontsize=25)

    else:
        screen.draw.text("You win!!!", (150, 200), color="blue", fontsize=50)
        time.sleep(2.5)




def on_mouse_move(pos):
    x = pos[0]
    my_paddle.position[0] = x


def update_ball(dt, paddle_x, paddle_y):
    global ball_speed_x, ball_speed_y
    ball.position.x -= ball_speed_x
    ball.position.y -= ball_speed_y

    if (ball.position.x >= WIDTH) or (ball.position.x <= 0):
        ball_speed_x *= -1
    if (ball.position.y >= HEIGHT) or (ball.position.y <= 0):
        ball_speed_y *= -1
    if ((paddle_x + 100) >= ball.position.x >= paddle_x) and (paddle_y <= ball.position.y):
        ball_speed_y *= -1

    if ball.position.y >= HEIGHT:
        ball.position.x = WIDTH // 2
        ball.position.y = HEIGHT // 2
        if hearts:
            hearts.pop()
            ball_speed_y += 1





def update(dt):
    update_ball(dt, my_paddle.position[0], my_paddle.position[1])






pgzrun.go()
