from projectile import Projectile
import math

class Missile(Projectile):
    def __init__(self, x,y, angle, color):
        Projectile.__init__(self, x, y, angle, 2.5, color)