import pygame
from pygame.locals import*

pygame.init()

width = 800
height = 800
road_w = int(width/1.6)


screen = pygame.display.set_mode((width, height))
screen.fill((60, 220, 0)) # Set the background colour
pygame.display.update()

run = True
while run:
    # Events
    for event in pygame.event.get():
        # If the exit button is clicked - exit
        if event.type == QUIT:
            run = False

pygame.quit()