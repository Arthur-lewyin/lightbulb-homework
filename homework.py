import pygame
import time

pygame.init()

WIDTH =  600
HEIGHT = 600 
scale = (WIDTH,HEIGHT)

display_surface = pygame.display.set_mode((WIDTH,HEIGHT)) 

pygame.display.set_caption("light switch")

on = pygame.image.load('on.jpg')
off = pygame.image.load("off.jpeg")

I_on=  pygame.transform.scale(on,scale)
I_off=  pygame.transform.scale(off,scale)

font =pygame.font.SysFont("Times New Roman",72)

t1 = font.render("crazy",True, (255,255,0))
t2 = font.render("crazy",True, (0,255,0))

while True:
    display_surface.blit(I_on,(0,0))
    display_surface.blit(t1,(200,200))
    pygame.display.update()
    time.sleep(1) 
    display_surface.blit(I_off,(0,0))
    display_surface.blit(t2,(200,200))
    pygame.display.update()
    time.sleep(1)

