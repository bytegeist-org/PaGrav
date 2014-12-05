import pygame
import sys
from pygame.locals import *

from Particle import *

pygame.init()

# define variables
# colors
black = (0, 0, 0)
white = (255, 255, 255)
# dimensions
screenwidth = 1024
screenheight = 768
fps = 24
# object coordinates
circle_x = screenwidth / 2
circle_y = screenheight / 2

# create screen
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption('PaGrav Visualisation')

# create clock
fpsTime = pygame.time.Clock()

# create particle
m1 = Particle(1, array([0, 0, 0]), array([25, 0, 0]))
m1.force = array([0, 1, 0])

while True:
    # blank screen
    screen.fill(black)

    # draw objects
    pygame.draw.circle(screen, white, (int(m1.location[0]),
    int(m1.location[1])), 5)
    # update state of particle
    m1.update_state(1)

    # handle events
    for event in pygame.event.get():
        # print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #update display
    fpsTime.tick(fps)
    pygame.display.update()