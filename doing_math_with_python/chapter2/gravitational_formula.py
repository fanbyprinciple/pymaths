'''
The relationship between gravitational force and
distance between two bodies
'''

import matplotlib.pyplot as plt 
from pylab import savefig

# Draw the graph
def draw_graph(x,y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters.')
    plt.ylabel('Gravitational force in Newton.')
    plt.title('Gravitational force and distance')
    plt.show()
    savefig('gravity.png')

def generate_F_r():
    # generate values for r
    r = range(100, 1001, 50)

    # Empty list
    F = []

    # Constant, G
    G = 6.674 * (10 **-11)
    # two masses
    m1 = 0.5
    m2 = 1.5

    # Calculate force andadd it to the list, F
    for dist in r:
        force = G* (m1 * m2)/ (dist ** 2)
        F.append(force)
    
    # call the draw_graph function
    draw_graph(r, F)

if __name__ == '__main__':
    generate_F_r()