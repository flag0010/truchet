from matplotlib.patches import Polygon
from matplotlib import pyplot as plt
from random import choice
from itertools import cycle
from math import cos, sin, radians as rad

class Truchet:
    #  locations defined as:
    #  a           b
    #  -------------
    #  |           |
    #  |  center   |
    #  |           |
    #  -------------
    #  c           d
    #
    def __init__(self, xcenter, ycenter, style):
        self.a, self.b, self.c, self.d = [xcenter-.5, ycenter+.5],[xcenter+.5, ycenter+.5],  [xcenter-.5, ycenter-.5], [xcenter+.5, ycenter-.5]
        if style == 'lowleft':
            self.p = [self.a, self.c, self.d]
        if style == 'lowright':
            self.p = [self.c, self.d, self.b]
        if style == 'upleft':
            self.p = [self.a, self.b, self.c]
        if style == 'upright':
            self.p = [self.a, self.b, self.d]
    def return_tile(self):
        return Polygon(self.p, closed=False, color='k')

class Truchet2:    
    #  modified truchet using 2 arcs
    def __init__(self, xcenter, ycenter, style):
        self.a, self.b, self.c, self.d = [xcenter-.5, ycenter+.5],[xcenter+.5, ycenter+.5],  [xcenter-.5, ycenter-.5], [xcenter+.5, ycenter-.5]
        if style == 1:  #upper right and lower left arcs
            #first upper right
            x = [self.b[0] + cos(rad(i))/2. for i in range(180, 271)]
            y = [self.b[1] + sin(rad(i))/2. for i in range(180, 271)]
            self.p1 = [x,y]
            #now lower left
            x = [self.c[0] + cos(rad(i))/2. for i in range(0, 91)]
            y = [self.c[1] + sin(rad(i))/2. for i in range(0, 91)]
            self.p2 = [x,y]
        if style == 2:  #upper left and lower right arcs
            #first upper left
            x = [self.a[0] + cos(rad(i))/2. for i in range(270, 361)]
            y = [self.a[1] + sin(rad(i))/2. for i in range(270, 361)]
            self.p1 = [x,y]
            #now lower right
            x = [self.d[0] + cos(rad(i))/2. for i in range(90, 181)]
            y = [self.d[1] + sin(rad(i))/2. for i in range(90, 181)]
            self.p2 = [x,y]
    def return_coords(self):
        return self.p1, self.p2


        
ax = plt.gca()

c = cycle(['lowleft',  'upleft'])#,'lowright',  'upleft'])
for i in range(20):
    for j in range(20):
        #random
        a = Truchet(i, j, choice(['lowleft', 'lowright', 'upleft', 'upright'])).return_tile()
        #cycle 4
        #a = Tile(i, j, c.next()).return_tile()
        ax.add_patch(a)

ax.set_xlim(-2,21)
ax.set_ylim(-2,21)        
plt.show()

for i in range(20):
    for j in range(20):
        p1, p2 = Truchet2(i,j, choice([1,2])).return_coords()
        plt.plot(p1[0], p1[1], color='k')
        plt.plot(p2[0], p2[1], color='k')
plt.show()
