# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


import math,random
from PIL.ImageTk import PhotoImage
from mobilesimulton import Mobile_Simulton
from missile import Missile

class Floater(Mobile_Simulton):
    radius = 5
    
    def __init__(self, x,y):
        Mobile_Simulton.__init__(self,x,y,Floater.radius*2,Floater.radius*2,random.random()*math.pi*2,5)
        self._image = PhotoImage(file='ufo.gif')      

    def update(self): 
        self.move()
        r = random.random()
        if r < 0.3:
            speed_change = random.randrange(-5,6)/10
            angle_change = random.randrange(-5,6)/10
            self.set_speed(self.get_speed() + speed_change)
            self.set_angle(self.get_angle() + angle_change)
            if self.get_speed() > 7:
                self.set_speed(7)
            if self.get_speed() < 3:
                self.set_speed(3)
        r = random.random()
        if r < 0.1: #shoots a missile downwards 10% of the time
            x,y = self.get_location()
            return Missile(x, y + 10, math.pi/2, 'blue')
        
        
    def display(self, canvas):
        canvas.create_image(*self.get_location(),image=self._image)