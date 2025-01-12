import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_triangle():
    # Initialize PyGame
    pygame.init()

    # Set up the display (500x500 window with OpenGL)
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 500, 0, 500)

    # Main loop for OpenGL rendering
    while True:
        glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen

        # Draw the triangle (Purple color)
        glBegin(GL_TRIANGLES)
        glColor3f(0.5, 0.0, 0.5)  # Purple color
        glVertex2f(250, 400)  # Top vertex
        glVertex2f(200, 300)  # Bottom-left vertex
        glVertex2f(300, 300)  # Bottom-right vertex
        glEnd()

        pygame.display.flip()  # Update the display

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

# Run the draw_triangle function
if __name__ == "__main__":
    draw_triangle()
