import pygame
import sys
from pygame.locals import *
from random import *

from ParticleSystem import *


pygame.init()

# define variables
# colors
black = (0, 0, 0)
white = (255, 255, 255)
# dimensions
screenwidth = 1280
screenheight = 800
fps = 30
# object coordinates
mid_x = screenwidth / 2
mid_y = screenheight / 2
# initialize font
myfont = pygame.font.SysFont("monospace", 25)
# initialize time
time = 0;
timestep = 10

# create screen
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption('PaGrav Visualisation')

# create clock
fpsTime = pygame.time.Clock()

# create particle
# m1 = Particle(1, array([0, 0, 0]), array([25, 0, 0]))
# m1.force = array([0, 1, 0])

# create three particles
m0 = Particle(1000000000000, array([mid_x, mid_y, 0]), array([0, 0, 0]))
m0.diameter = 15
m1 = Particle(1000, array([mid_x-300, mid_y-300, 0]), array([0.3, -0.1, 0]))
m1.diameter = 6
m2 = Particle(1000, array([mid_x, mid_y + 300, 0]), array([-0.4, 0, 0]))
m2.diameter = 6
m3 = Particle(1000000, array([mid_x, mid_y - 300, 0]), array([0.5, 0, 0]))
m3.diameter = 10
m4 = Particle(1000000, array([mid_x-400, mid_y-200, 0]), array([0.2, -0.2, 0]))
m4.diameter = 10

# setup particle system
sys = ParticleSystem(m0)
sys.add_particle(m1)
sys.add_particle(m2)
sys.add_particle(m3)
sys.add_particle(m4)

# add random particles
for i in range(20):
    sys.add_particle(Particle(1, array([randint(0,screenwidth),
        randint(0,screenheight), 0]), array([randint(-50,50)/100.,
        randint(-50,50)/100., 0])))

nb_of_particles = len(sys.particles)

while True:
    # blank screen
    screen.fill(black)

    # add grav forces
    for x in range(nb_of_particles):
        fx = sys.calculate_gravitational_force(x)
        sys.particles[x].add_force(fx)

    # update state of particle
    sys.update_state(timestep)
    time += timestep

    # draw objects
    for x in range(nb_of_particles):
        pygame.draw.circle(screen, white, (int(sys.particles[x].location[0]),
        int(sys.particles[x].location[1])), sys.particles[x].diameter)
    # render text
    label = myfont.render("Time: " + str(time), 1, (255,255,0))
    screen.blit(label, (10, 10))

    # clear forces
    sys.clear_forces()

    # handle events
    for event in pygame.event.get():
        # print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #update display
    fpsTime.tick(fps)
    pygame.display.update()