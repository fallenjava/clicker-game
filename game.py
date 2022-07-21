import sys, pygame

pygame.init()


size = width, height = 320, 240



screen = pygame.display.set_mode(size)


running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: running = False
