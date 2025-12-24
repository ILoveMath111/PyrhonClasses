import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Screen Elements")

# Set up font
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw a red rectangle at (100, 100) with width 200 and height 100
    pygame.draw.rect(screen, RED, (100, 100, 200, 100))

    # Render text surface
    text_surface = font.render("Hello Pygame!", True, BLACK)

    # Get the rectangle object for the text surface and set its position
    text_rect = text_surface.get_rect()
    text_rect.topleft = (100, 250)

    # Blit the text onto the screen
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()