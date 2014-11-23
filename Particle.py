#A Particle class

from numpy import *


class Particle:
    """A simple particle class"""
    def __init__(self, mass, location, velocity):
        self.mass = mass
        self.location = location    # numpy array [sx,sy,sz]
        self.velocity = velocity    # numpy array [vx,vy,vz]
