#If a projectile hits any simulton in its path,
#that simulton is destroyed. The missile itself
#is also destroyed. The missile is also removed 
#from the canvas if it goes off the screen.
#Missiles can also knock out other missiles
from mobilesimulton import Mobile_Simulton
from PIL.ImageTk import PhotoImage
import math

class Projectile(Mobile_Simulton):
    
    def __init__(self, x,y, angle, radius, color):
        self.radius = radius
        self.color = color
        Mobile_Simulton.__init__(self, x, y, radius*2, radius*2, angle, 8)
    
    #return whether it hits another simulton
    def hit(self, s:'Simulton'):
        w1 = self.get_dimension()[0]
        w2 = s.get_dimension()[0]
#         print(self.distance(s.get_location())- w1/2 -w2/2)
        return self.distance(s.get_location()) - w1/2 -w2/2 <=0
    
    #unlike other mobile simultons, missle does not bounce of the sides
    def move(self):
        self.change_location(self._speed*math.cos(self._angle),
                             self._speed*math.sin(self._angle))
        
    #returns the simulton that the missile hit
    def update(self, simultons:'list of simultons'):
        self.move()
        for s in simultons:
            if self.hit(s):
                return {s, self} #returns both, since both will be destroyed
        
    def display(self, canvas):
        canvas.create_oval(self._x-self.radius, self._y-self.radius,
                           self._x+self.radius, self._y+self.radius,
                           fill = self.color)
        