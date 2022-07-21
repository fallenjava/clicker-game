import pygame

pygame.init()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)

clicks = 0

running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: 
            running = False

        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                clicks += 1

