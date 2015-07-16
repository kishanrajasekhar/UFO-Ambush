#A spaceship is meant to be controlled
#by users. It's actions is determined 
#by a 'key' parameter, representing the keyboard input
#of the user. The ship has two images: one in its
#normal state and one in its re-charge state.


from mobilesimulton import Mobile_Simulton
import model
from PIL.ImageTk import PhotoImage
import math
from missile import Missile


class Space_ship(Mobile_Simulton):

    def __init__(self,x ,y, speed, recharge_time, capacity):
        '''Introduces two new attributes: recharge_time and capacity (for ammo)'''
        Mobile_Simulton.__init__(self, x, y, 10, 10, 0, speed)
        self._image = PhotoImage(file = "spaceship.gif")
        self._recharge_image = PhotoImage(file = "spaceship_recharge.gif")
        #new attributes
        self.charge = 0 #the charge time after the ship runs out of ammo
        self.bullets = capacity #ship starts out with fully loaded ammunition
        self.capacity = capacity #the max amount of ammo that the ship can carry
        self.recharge_time = recharge_time #the amount of time that it takes for the ship to reload 
        
        
    def update(self, key):
        '''The key parameter determines which direction the ship moves or fires a bullet.
        The ship is meant to be controlled by a user. There can only be one action per
        update.'''
        #move left
        if key == "'a'":
            self.set_angle(math.pi)
            self.move()
        #move right
        if key == "'d'":
            self.set_angle(0)
            self.move()
            
        #The ship cannot fire if it ran out of bullets
        if self.bullets <= 0:
            return
        
        #Fire straight up
        if key == "'w'":
            x,y = self.get_location()
            self.bullets -= 1
            return Missile(x, y-10, 3*math.pi/2, 'red')
        #Fire 45 degrees to the left
        if key == "'q'":
            x,y = self.get_location()
            self.bullets -= 1
            return Missile(x, y-10, 5*math.pi/4, 'red')
        #Fire 45 degrees to the right
        if key == "'e'":
            x,y = self.get_location()
            self.bullets -= 1
            return Missile(x, y-10, 7*math.pi/4, 'red')
        
    def recharge(self):
        '''If the ship runs out of bullets, it needs to spend time recharging. During this
        time, the ship is defenseless'''
        if self.bullets <= 0:
            self.charge += 1
            if self.charge > self.recharge_time:
                self.bullets = self.capacity
                self.charge = 0
                
    def is_recharging(self):
        '''Returns whether the ship is recharging or not.'''
        return self.bullets <= 0
                
    def add_bullets(self, number):
        '''Adds the specified number of bullets to the ship as long as it does not 
        exceed the ship's capacity'''
        self.bullets += number
        if self.bullets > self.capacity:
            self.bullets = self.capacity
            
    def get_num_bullets(self):
        '''Return the number of bullets the ship currently has. If it does not have any
        bullets, the message 'Recharging ammunition' is returned instead'''
        if self.bullets <= 0:
            return "Recharging ammunition"
        return self.bullets

    def display(self, canvas):
        '''The space ship image is a small icon I made using Microsoft Paint :P'''
        if self.bullets <= 0: #spaceship is recharging
            canvas.create_image(*self.get_location(),image=self._recharge_image)
        else:
            canvas.create_image(*self.get_location(),image=self._image)