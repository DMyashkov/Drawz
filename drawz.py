import pygame
import random
import os

import constants as c

pygame.init()

screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

is_drawing = False
drawing_color = c.BLACK
drawing_surface = pygame.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
drawing_surface.fill(c.WHITE)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                is_drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if is_drawing:
                x, y = pygame.mouse.get_pos()
                pygame.draw.circle(drawing_surface, drawing_color, (x, y), 5)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                drawing_surface.fill(c.WHITE)
            elif event.key == pygame.K_q:
                running = False
    
    screen.fill(c.WHITE)
    
    screen.blit(drawing_surface, (0, 0))

    pygame.display.flip()

    clock.tick(60)

# Quit the game
pygame.quit()