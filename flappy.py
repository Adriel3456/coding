import pgzrun
from random import randint

TITLE = "Flappy Ball"
WIDTH = 800
HEIGHT = 600

R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
CLR = R,G,B

#BLUE = o, 128, 255
GRAVITY = 2000.0 # pixels per second per seconds


class ball:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)


ball = ball(50, 100)
ball1 = ball(200, 100)


def draw():
    screen.clear()
    ball.draw()
    ball1.draw()


def update(dt):
    # Apply constant acceleration forumla
    uy = ball.vy
    ball.vy += GRAVITY * dt
    ball.y += (uy + ball.vy) * 0.5 * dt 

    uy = ball1.vy
    ball1.vy += GRAVITY * dt 
    ball1.y +- (uy + ball1.vy) * 0.5 * dt 

    # detect and handle bounce
    if ball.y > HEIGHT - ball.radius: # we've bounced!
        ball.y =  HEIGHT - ball.radius # fix the position
        ball.vy= -ball1.vy * 0.9







    ball.x += ball.vx * dt 
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

    
    ball1.x += ball1.vx * dt
    if ball.x > WIDTH - ball1.radius or ball1.x < ball1.radius:
        ball1.vx = -ball1.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = -500
        ball1.vy = -500


pgzrun.go()