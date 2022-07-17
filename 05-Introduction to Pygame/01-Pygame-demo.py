# Import Packages
import pygame
from pygame.locals import *
import sys
from pathlib import Path


# Define Constants
pathToBall = Path('05-Introduction to Pygame/images/ball.png')
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock() 

# Load assets: images and sounds
ballImage = pygame.image.load('/home/kevin/Desktop/github projects/Object-Oriented-Programming-with-Python/05-Introduction to Pygame/images/ball.png')

# Initialize variables

# Loop forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# Do any per frame actions


# Clear window
window.fill(BLACK)

# Draw all window elements
window.blit(ballImage, (100,200))
pygame.display.update()

# Slow things down a bit
clock.tick(FRAMES_PER_SECOND) 
