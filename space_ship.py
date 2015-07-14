from mobilesimulton import Mobile_Simulton
import model
from PIL.ImageTk import PhotoImage
import math
from missile import Missile


class Space_ship(Mobile_Simulton):
    SPEED = 5
    RECHARGE_TIME = 50 #time needed to re equip on bullets
    CAPACITY = 15 #number of bullets ship can carry

    def __init__(self,x ,y):
        Mobile_Simulton.__init__(self, x, y, 10, 10, 0, Space_ship.SPEED)
        self._image = PhotoImage(file = "spaceship.gif")
        self._recharge_image = PhotoImage(file = "spaceship_recharge.gif")
        self.bullets = Space_ship.CAPACITY #holds 
        self.charge = 0
        
    def update(self, key):
        if key == "'a'":
            self.set_angle(math.pi)
            self.move()
        if key == "'d'":
            self.set_angle(0)
            self.move()
        #firing bullets
        if self.bullets <= 0:
            return
        if key == "'w'":
            x,y = self.get_location()
            self.bullets -= 1
            return Missile(x, y-10, 3*math.pi/2, 'red')
        if key == "'q'":
            x,y = self.get_location()
            self.bullets -= 1
            return Missile(x, y-10, 5*math.pi/4, 'red')
        if key == "'e'":
            x,y = self.get_location()
            self.bullets -= 1
            return Missile(x, y-10, 7*math.pi/4, 'red')
        
    def recharge(self):
        if self.bullets <= 0:
            self.charge += 1
            if self.charge > Space_ship.RECHARGE_TIME:
                self.bullets = Space_ship.CAPACITY
                self.charge = 0
            
    def get_num_bullets(self):
        if self.bullets <= 0:
            return "Recharging ammunition"
        return self.bullets

    def display(self, canvas):
        if self.bullets <= 0: #spaceship is recharging
            canvas.create_image(*self.get_location(),image=self._recharge_image)
        else:
            canvas.create_image(*self.get_location(),image=self._image)