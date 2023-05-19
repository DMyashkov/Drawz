import pygame
import random
import os

import constants as c
#from .assets.objects import FallingImage
pygame.init()

#Variables
falling_images = []

#Set up the game window
screen = pygame.display.set_mode((c.screen_width, c.screen_height))

#Set up the game clock
clock = pygame.time.Clock()

# Set up the drawing surface
drawing_surface = pygame.Surface((c.screen_width, c.screen_height))
drawing_points = []  # Store the drawing points

def generate_image_position():
    x = random.randint(0, c.screen_width - c.image_width)
    y = random.randint(0, c.screen_height - c.image_height)
    return x, y

running = True
drawing = False  # Flag to indicate if the player is drawing

image_files = os.listdir(c.image_folder)

for filename in image_files:
    # Construct the full file path
    file_path = os.path.join(c.image_folder, filename)
    
    # Load the image using pygame.image.load()
    image = pygame.image.load(file_path)
    
    # Resize the image to desired dimensions
    image = pygame.transform.scale(image, (c.image_width, c.image_height))
    
    # Generate initial positions for the falling images
    x, y = generate_image_position()
    
    # Append the image and its position to the falling_images list
    falling_images.append({
        'image': image,
        'position': [x, y]
    })

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button pressed
                drawing = True
                drawing_points = []  # Clear the previous drawing points
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button released
                drawing = False
                
                # Pass the drawing surface to AI for recognition
                # Convert the drawing surface to an appropriate representation (e.g., numpy array)
                # Feed the representation to your AI model for recognition
                
                # Compare recognized drawing with falling images
                # Update game logic based on the result
                
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                mouse_pos = pygame.mouse.get_pos()
                drawing_points.append(mouse_pos)
    
    # Redraw the screen
    screen.fill(c.WHITE)
    for image_data in falling_images:
        x, y = image_data['position']
        screen.blit(image_data['image'], (x, y))
    pygame.display.flip()
    
    # Draw the drawing surface on the screen
    if len(drawing_points) > 1:
        pygame.draw.lines(drawing_surface, c.BLACK, False, drawing_points, 2)

    # Control the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()