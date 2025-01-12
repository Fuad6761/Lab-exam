import pygame
import sys

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the screen (500x400 window)
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("My Canvas")

    # Fill the canvas with a white color
    screen.fill((255, 255, 255))

    # Update the display to show the white canvas
    pygame.display.flip()

    # Main loop to keep the window open and handle events
    while True:
        for event in pygame.event.get():
            # Check if the Space key is pressed to quit
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pygame.quit()  # Quit Pygame
                sys.exit()  # Exit the program

if __name__ == "__main__":
    main()
