import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()
pygame.display.init()
size = width, height = 800, 600
font = pygame.font.SysFont('assets/Poppins-ExtraLight.ttf', 64)
cursor = pygame.image.load("assets/cursor.png") 
cursor_clicked = pygame.image.load("assets/cursor_click.png")
icon = pygame.image.load('assets/icon.png')
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Clicker Game")
pygame.display.set_icon(icon)
clicks = 0

running = True
while running:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicks += 1 
                print(clicks)

        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                clicks += 1
                print(clicks)
        
            
    text = font.render("Clicks: " + str(clicks), True, (0, 0, 0))
    screen.fill((255, 255, 255))
    screen.blit(text, (300, 100))
    pygame.display.flip()

