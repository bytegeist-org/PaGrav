from ParticleSystem import *
import matplotlib.pyplot as plt

m1 = Particle(100, array([0, 0, 0]), array([0, 0, 0]))
m2 = Particle(10, array([10, 10, 0]), array([1, 1, 0]))
m3 = Particle(150, array([10, 5, 0]), array([1, 5, 0]))

sys = ParticleSystem(m1)
sys.add_particle(m2)
sys.add_particle(m3)

print sys.particles[0].mass
print sys.particles[1].mass
print sys.particles[2].mass

print sys.calculate_distance(0, 1)

nb_part = len(sys.particles)
matrix = zeros((nb_part, nb_part))
print matrix

for x in range(nb_part):
    for y in range(nb_part):
        matrix[x, y] = sys.calculate_distance(x, y)

print matrix

print "sosososo..."

print "distance matrix:"
print sys.calculate_distance_matrix()

print "direction vector:"
print sys.calculate_direction_vector(0, 1)
print sys.calculate_direction_vector(0, 2)




# for x in range(nb_part):
#     plotx.append(sys.particles[x].location)
#     ploty.append()
#
# plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()

#print array([10,10,0])/14.1421356237
