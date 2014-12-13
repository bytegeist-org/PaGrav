#A Particle class

from numpy import *


class Particle:
    """A simple particle class"""
    def __init__(self, mass, location, velocity):
        self.mass = float(mass)
        self.location = location        # numpy array [sx,sy,sz]
        self.velocity = velocity        # numpy array [vx,vy,vz]
        self.force = array([0, 0, 0])   # numpy array [Fx,Fy,Fz]
        self.diameter = 1

    def add_force(self, new_force):
        """add a force (numpy array [Fx, Fy, Fz])to particle"""
        self.force = self.force + new_force

    def clear_force(self):
        """set force which affects particle to zero"""
        self.force = array([0, 0, 0])

    def update_state(self, timestep):
        """update location and velocity according to force"""
        # update location
        self.location = ((1 / self.mass) * timestep ** 2 * self.force +
                        self.velocity * timestep +
                        self.location)
        # update velocity
        self.velocity = ((1 / self.mass) * timestep * self.force +
                        self.velocity)