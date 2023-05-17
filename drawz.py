import pygame
import random

import constants as c
from .assets.objects import FallingImage
pygame.init()

#Variables
falling_images = []

#Set up the game window
screen = pygame.display.set_mode((c.screen_width, c.screen_height))

#Set up the game clock
clock = pygame.time.Clock()

def generate_image_position():
    x = random.randint(0, c.screen_width - c.image_width)
    y = random.randint(-c.screen_height, -c.image_height)
    return x, y

for _ in range(5):  # Number of initial falling images
    x, y = generate_image_position()
    falling_images.append({
        'image': FallingImage,
        'position': [x, y]
    })

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Handle user input

    # Move falling images

    # Redraw the screen
    screen.fill(c.BLACK)
    for image_data in falling_images:
        x, y = image_data['position']
        screen.blit(image_data['image'], (x, y))
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()