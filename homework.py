import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Shape Drawer")

WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
GREEN = (0, 200, 0) 
RED = (255, 60, 60)
YELLOW = (255, 255, 0)

screen.fill(WHITE)

# Rectangle
pygame.draw.rect(screen, BLUE, (50, 50, 150, 80))

# Square
pygame.draw.rect(screen, GREEN, (250, 50, 100, 100))

# Circle
pygame.draw.circle(screen, RED, (130, 250), 60)

# Triangle
pygame.draw.polygon(screen, YELLOW, [(350, 200), (450, 350), (250, 350)])

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
