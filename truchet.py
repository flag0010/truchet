from matplotlib.patches import Polygon
from matplotlib import pyplot as plt
from random import choice
from itertools import cycle

class Tile:
    ##locations defined as
    #a           b
    #-------------
    #|           |
    #|  center   |
    #|           |
    #-------------
    #c           d
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
        
ax = plt.gca()

c = cycle(['lowleft',  'upleft'])#,'lowright',  'upleft'])
for i in range(20):
    for j in range(20):
        #random
        a = Tile(i, j, choice(['lowleft', 'lowright', 'upleft', 'upright'])).return_tile()
        #cycle 4
        #a = Tile(i, j, c.next()).return_tile()
        ax.add_patch(a)

ax.set_xlim(-2,21)
ax.set_ylim(-2,21)        
plt.show()
