#Class of Particle System

from numpy import *
from Particle import *


class ParticleSystem:
    """A System of partices"""
    particles = []

    def __init__(self, first_particle):
        self.particles.append(first_particle)

    def add_particle(self, particle):
        self.particles.append(particle)

    def calculate_distance(self, particle_nb_1, particle_nb_2):
        """returns the distance between two system"""
        return linalg.norm(self.particles[particle_nb_2].location -
                           self.particles[particle_nb_1].location)

    def calculate_distance_matrix(self):
        """returns the distance between all system of the system as a
        matrix"""
        # moegliche optimierung: nur die untere haelfte der Matrix berechnen und
        # nach oben spiegeln
        nb_of_system = len(self.particles)
        distance_matrix = zeros((nb_of_system, nb_of_system))
        for x in range(nb_of_system):
            for y in range(nb_of_system):
                distance_matrix[x, y] = self.calculate_distance(x, y)
        return distance_matrix

    def calculate_direction_vector(self, particle_nb_1, particle_nb_2):
        """calculate direction vector"""
        # Richtungsvektor
        xy = self.particles[particle_nb_2].location - self.particles[particle_nb_1].location
        # Abstand
        distance_xy = self.calculate_distance(particle_nb_1, particle_nb_2)
        # Einheitsvektor bestimmen
        e_xy = xy / distance_xy
        #print e_xy
        return e_xy
