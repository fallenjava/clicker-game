import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()
pygame.display.init()
size = width, height = 800, 600
font = pygame.font.Font('assets/Poppins-ExtraLight.ttf', 64)
font2 = pygame.font.Font('assets/Poppins-ExtraLight.ttf', 48) 
cursor = pygame.image.load("assets/cursor.png") 
cursor_clicked = pygame.image.load("assets/cursor_click.png")
icon = pygame.image.load('assets/icon.png')
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Clicker Game")
pygame.display.set_icon(icon)
clicks = 0
hundredclicks = ("Reached 100 Clicks")
thousandclicks = ("Reached 1000 Clicks")

running = True
while running:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicks += 1 
                print(clicks)
                if clicks == 100:
                    print(hundredclicks)
                if clicks == 1000:
                    print(thousandclicks)
        
   
        
            
    text = font.render("Clicks: " + str(clicks), True, (0, 0, 0))
    if clicks == 100:
        text = font2.render(str(hundredclicks), True, (0, 0, 0))
    elif clicks == 1000:   
        text = font2.render(str(thousandclicks), True, (0, 0, 0))
    screen.fill((255, 255, 255))
    screen.blit(text, (269, 100))
    pygame.display.flip()

