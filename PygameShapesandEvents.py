import pygame
import random
WIDTH = 800
HEIGHT = 700
TITLE = "Pygame shapes and events"

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

class Circle:
    def __init__(self,radius,x,y,color):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
 
    def draw_circle(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
circle1 = Circle(30,400,350,"tomato")

run = True

while run == True:
    screen.fill("SeaGreen")
    circle1.draw_circle()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle1.radius += 10
            if event.button == 4:
                circle1.radius -= 10
        if event.type == pygame.MOUSEBUTTONUP:
            colours = ["white","green","blue","yellow","orange","pink","purple","red"]
            circle1.color = random.choice(colours)
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            circle1.x,circle1.y = pos
        
    pygame.display.update()
