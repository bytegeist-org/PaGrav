from ParticleSystem import *
import matplotlib.pyplot as plt

# create three particles
m1 = Particle(1, array([0, 0, 0]), array([0, 0, 0]))
m2 = Particle(1000000, array([1, 0, 0]), array([1, 1, 0]))
m3 = Particle(150, array([0, 1, 0]), array([1, 5, 0]))
m4 = Particle(100, array([0, 5, 0]), array([0, 0, 0]))

# setup particle system
sys = ParticleSystem(m1)
sys.add_particle(m2)
sys.add_particle(m3)
#sys.add_particle(m4)

## print masses of particles
#print(sys.particles[0].mass)
#print(sys.particles[1].mass)
#print(sys.particles[2].mass)

##test calculate_distance
## print distance between m0 and m1
#print(sys.calculate_distance(0, 3))

##test distance matrix
## print distance matrix:
#print("distance matrix:")
#sys.calculate_distance_matrix()
#print(sys.distance_matrix)
#print(sys.distance_matrix[0, 2])

##test direction vektor
#print "direction vector:"
## print direction vector from m0 to m1:
#print(sys.calculate_direction_vector(0, 1))
## print direction vector from m0 to m2:
#print(sys.calculate_direction_vector(0, 2))
## print direction vector from m0 to m3:
#print(sys.calculate_direction_vector(0, 3))

##test add_force and clear_force
#print("force of particle")
#print(m4.force)
#m4.add_force(array([1, 0, 0]))
#print(m4.force)
#m4.add_force(array([1, 0, 0]))
#print(m4.force)
#m4.clear_force()
#print(m4.force)


#m1.force = array([0, 0, 1])
#m2.force = array([0, 3, 3])
#print(m1.location)
#for i in range(10):
    #print(m1.location)
    #print(m1.velocity)
    #m1.update_state(1)

print(len(sys.particles))
test_force = sys.calculate_gravitational_force(0)
print (test_force)