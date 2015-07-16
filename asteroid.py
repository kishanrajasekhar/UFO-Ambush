#An asteroid is a large Projectile.

from projectile import Projectile
import math

class Asteroid(Projectile):
    def __init__(self, x,y):
        Projectile.__init__(self, x, y, math.pi/2, 10, "gray")