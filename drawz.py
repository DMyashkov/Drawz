import pygame
import random
import os
import numpy as np
from PIL import Image

from dynamic import txt_name_list

from keras.models import load_model
model = load_model('model.h5')

import constants as c

pygame.init()

screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pygame.display.set_caption("Doodle Recognition")

is_drawing = False
drawing_color = c.BLACK
drawing_surface = pygame.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
drawing_surface.fill(c.WHITE)

running = True
clock = pygame.time.Clock()

# Set up variables for capturing screen
capture_interval = 0.5  # Capture screen every 0.5 seconds
last_capture_time = 0


print(txt_name_list)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            recognize_flag = True
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
            if event.key == pygame.K_SPACE:
                # Capture the drawn image
                pygame.image.save(drawing_surface, 'drawing.png')
                # Resize and preprocess the image
                image = Image.open('drawing.png').convert('L')
                #create file to save image
                image = image.resize((28, 28))
                image.save('drawing2.png')
                image_data = np.array(image)
                image_data = image_data.astype('float32') / 255.
                image_data = np.reshape(image_data, (1, 28, 28, 1))
                
                # Predict the digit
                print(model.predict(image_data))
                predictions = model.predict(image_data)[0]
                i = 0
                for prediction in predictions:
                    print("Prediction"+ str(i) + " - " + str(prediction))
                    i+=1
                predicted_class_index = np.argmax(predictions)
                predicted_class_name = txt_name_list[predicted_class_index]

                # Display the prediction on the screen
                font = pygame.font.Font(None, 36)
                #text = font.render("Prediction: " + predicted_class_name, True, (255, 255, 255))
                print("Prediction: " + predicted_class_name)
                #drawing_surface.blit(text, (10, 10))
                pygame.display.update()
            if event.key == pygame.K_r:
                drawing_surface.fill(c.WHITE)
                pygame.display.update()

    
    screen.fill(c.WHITE)
    
    screen.blit(drawing_surface, (0, 0))

    pygame.display.flip()

    clock.tick(60)


# Quit the game
pygame.quit()