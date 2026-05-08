import pgzrun

WIDTH = 800
HEIGHT = 700
TITLE = "Flappy Ball"
GRAVITY = 1000

class Ball:
    def __init__(self,radius,x,y,color):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.vx = 50
        self.vy = 0
    
    def drawball(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,self.color)

ball1 = Ball(20,400,350,"yellow")

def draw():
    screen.fill("LightSkyBlue")
    ball1.drawball()


def update(dt):
    uy = ball1.vy
    ball1.vy += GRAVITY * dt
    ball1.y += (uy + ball1.vy) * 0.5 * dt
    if ball1.y >= 680:
        ball1.vy = ball1.vy * -1
    
    ball1.x += ball1.vx * dt
    if ball1.x >= 780:
        ball1.vx = ball1.vx * -1
    if ball1.x <= 20:
        ball1.vx = ball1.vx * -1
pgzrun.go()