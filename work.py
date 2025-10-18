import pygame
import time

pygame.init()

HEIGHT = 600
WIDTH = 600

display_surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("birthday greeting card")

img=pygame.image.load("birthdayone.jpg")
image = pygame.transform.scale(img, (WIDTH,HEIGHT))

while (True):
    font=pygame.font.SysFont("Times New Roman", 72)
    text=font.render("Happy",True,(0,0,0))
    text2=font.render("Birthday",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image,(0,0))
    display_surface.blit(text,(210,180))
    display_surface.blit(text2,(180,264))
    pygame.display.update()
    time.sleep(2)
    

    img2=pygame.image.load("birthdaytwo.jpg")
    
    text1=font.render("You have a good birthday",True,(0,0,0))
    text3=font.render("You are older now too",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image,(0,0))
    display_surface.blit(text1,(110,180))
    display_surface.blit(text3,(110,264))
    pygame.display.update()
    time.sleep(2)