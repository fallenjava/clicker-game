import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()
size = width, height = 800, 600
font = pygame.font.SysFont('Poppins-ExtraLight.ttf')
cursor = pygame.image.load("cursor.png") 
cursor_clicked = pygame.image.load("cursor_click.png")

screen = pygame.display.set_mode(size)

clicks = 0

running = True
while running:

    for event in pygame.event.get():
        pygame.draw.rect()
        if event.type == pygame.QUIT: 
            running = False

        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                clicks += 1
                print(clicks)

