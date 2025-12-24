import pygame
import sys

# Initialize Pygame
pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the display (create the screen object)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("My First Game Screen")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill(WHITE)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()