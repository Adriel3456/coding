import pygame
pygame.init()
screen=pygame.display.set_mode((500, 500))
pygame.display.set_caption("Hello")

screen.fill((123, 223, 25))
pygame.draw.circle(screen, (255, 0, 0), (250,250), 50)
pygame.display.update()