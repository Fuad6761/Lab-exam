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

    # Draw Ethiopian flag: Green, Yellow, Red rectangles
    pygame.draw.rect(screen, (0, 128, 0), (50, 100, 400, 100))  # Green
    pygame.draw.rect(screen, (255, 255, 0), (50, 200, 400, 100))  # Yellow
    pygame.draw.rect(screen, (255, 0, 0), (50, 300, 400, 100))  # Red

    # Draw a purple point at the center of the flag
    pygame.draw.circle(screen, (128, 0, 128), (250, 250), 5)

    # Update the display to show the point
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
