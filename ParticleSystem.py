#Class of Particle System

from numpy import *
from Particle import *


class ParticleSystem:
    """A System of partices"""
    # constants
    GRAV_CONST = 6.67384e-11
    # variables
    particles = []
    distance_matrix = []

    def __init__(self, first_particle):
        self.particles.append(first_particle)

    def add_particle(self, particle):
        """add a particle to the system"""
        self.particles.append(particle)

    def update_state(self, timestep):
        """update state of all particles of system"""
        nb_of_particles = len(self.particles)
        for x in range(nb_of_particles):
            self.particles[x].update_state(timestep)

    def clear_forces(self):
        """update state of all particles of system"""
        nb_of_particles = len(self.particles)
        for x in range(nb_of_particles):
            self.particles[x].force = array([0, 0, 0])

    def calculate_distance(self, particle_nb_1, particle_nb_2):
        """returns the distance between two system"""
        return linalg.norm(self.particles[particle_nb_2].location -
                           self.particles[particle_nb_1].location)

    def calculate_distance_matrix(self):
        """calculates the distance between all particles of the system as a
        matrix"""
        # possible optimization: calculate only on half of the matrix and mirror
        # elements
        # number of particles
        nb_of_particles = len(self.particles)
        # create empty / clear matrix
        self.distance_matrix = zeros((nb_of_particles, nb_of_particles))
        # calculate elements of matrix
        for x in range(nb_of_particles):
            for y in range(nb_of_particles):
                self.distance_matrix[x, y] = self.calculate_distance(x, y)
        return self.distance_matrix

    def calculate_direction_vector(self, particle_nb_1, particle_nb_2):
        """calculate direction vector"""
        # direction vector
        xy = (self.particles[particle_nb_2].location -
              self.particles[particle_nb_1].location)
        # distance
        distance_xy = self.calculate_distance(particle_nb_1, particle_nb_2)
        # unit vector
        e_xy = xy / distance_xy
        return e_xy

    def calculate_gravitational_force(self, particle_nb):
        """calculate gravitational force on particles due to all other
        particles of the system"""
        # number of particles
        nb_of_particles = len(self.particles)
        # init sum of forces
        sum_of_forces = array([0., 0., 0.])
        abs_force = 0
        # sum up all single forces
        for x in range(nb_of_particles):
            if x != particle_nb:
                m1 = float(self.particles[x].mass)
                m2 = float(self.particles[particle_nb].mass)
                d = float(self.calculate_distance(x, particle_nb))
                dir_vector = self.calculate_direction_vector(particle_nb, x)
                # calculate force
                abs_force = self.GRAV_CONST * ((m1 * m2) / (d ** 2))
                sum_of_forces += dir_vector * abs_force
                #print dir_vector * abs_force
        return sum_of_forces