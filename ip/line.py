import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_line(x1, y1, x2, y2):
    """
    Draw a line between two points using PyGame and OpenGL.
    """
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display (500x500 window with OpenGL)
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 500, 0, 500)

    # Main loop for OpenGL rendering
    while True:
        glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen

        # Draw a red line from (100, 100) to (400, 400)
        draw_line(100, 100, 400, 400)

        pygame.display.flip()  # Update the display

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

# Run the main function
if __name__ == "__main__":
    main()
