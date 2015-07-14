#The model contains all the functions needed to run the game

import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update
from space_ship import Space_ship
from projectile import Projectile
import math, random
from asteroid import Asteroid
from floater import Floater

#Global variables for starting the game
first = True #when the simulation begins
second = False

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
pause = False
ship = None #this becomes the space ship that the player controls
simultons = set() # a set of simultons, starting with the ship
score = 0
update_count = 0 #keeps track of how many times the update all method is called
obstacles = {Asteroid:0.1, Floater:0.01} #obstacles and their appearance rate


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(), controller.the_canvas.winfo_height())



#how the initial screen setup should be, a spaceship on the bottom center of the 
#window 
def start():
    global simultons,ship, ASTEROID, pause
    w,h = world() #the widht and height of the world
    ship = Space_ship(w/2, h-10)
    simultons.add(ship) #add the ship that the player controls
    controller.the_pause_button["text"] = "Start Game!"
    controller.the_score.config(text = "Press Start Game!", width = 40)
    pause = True
    

#add simulton s to the simulation
def add(s):
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global simultons
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global simultons
    result = set()
    for s in simultons:
        if p(s):
            result.add(s)
    return result


#call update for every simulton in the simulation
def update_all():
    #intitial screen setup
    #for some reason, I have to use 2 global variables..I'm not sure why
    global first, second
    if second:
        start()
        second = False
    if first:
        first = False
        second = True
        
    #what happens every update after initialization
    else:
        global pause, simultons, score, ship, game_over, update_count
        ammunition = None #how much ammo the ship has
        #if any projectile is outside the canvas window
        outOfScreen = find(lambda s: isinstance(s,Projectile) and\
                 (s.get_location()[0] > controller.the_canvas.winfo_width()\
                 or s.get_location()[0] < 0) or (s.get_location()[1] < 0 or \
                 s.get_location()[1] > controller.the_canvas.winfo_height()))
        destroyed = set()
        new_objects = set()
        if not pause:
            if ship not in simultons: #game over
                controller.the_score.config(text = "Game Over. Score: " + str(score) +\
                 " \nPress Reset to play again", width = 40)
                return
            add_obstacle()
            for s in simultons:
                if s == ship:
                    ammunition = s.get_num_bullets()
                    s.recharge()
                    pass
                elif isinstance(s,Projectile):
                    targets = find(lambda t: t!= s) #every other simulton except the projectile itself
                    contact = s.update(targets)#might have to edit the update method
                    if contact != None: #if contact is actually a returned set
                        destroyed |= contact 
                elif isinstance(s, Floater):
                    new_objects.add(s.update())
            for obj in outOfScreen:
                simultons.remove(obj)
            for obj in destroyed:
                if isinstance(obj, Asteroid):
                    score += 1
                elif isinstance(obj, Floater):
                    score += 2
                simultons.remove(obj)
            simultons |= {new for new in new_objects if new != None}
            #update game information
            info = "Score: " + str(score) +\
                    "|Ammunition: " +str(ammunition)
            controller.the_score.config(text = info, width = 40)
            #increase difficulty every 100 updates
            update_count +=1
            if update_count > 100 and update_count%100 == 0:
                challenge_increase()
            
    
        
def add_obstacle(): #add asteroids to simulton list
    global simultons, obstacles
    r = random.random()
    obstacle = list(obstacles)[random.randrange(len(obstacles))] #randomly chosen obstacle
    if r < obstacles[obstacle]: #the appearance rate of the randomly chosen obstacle
        w,h = world()
        random_width = random.randrange(0,w)
        simultons.add(obstacle(random_width, 10))
        
def challenge_increase():
    global obstacles
    for o in obstacles:
        if obstacles[o] < .5: #putting limit at 50% appearance rate
            obstacles[o] += 0.01  #increases the appearance rate of the obstacles by 1%

def move_ship(event):
    global simultons, pause
    key = repr(event.char)
#     if key == "'r'": #allows players to reset game by pressing 'r'
#         reset()
#     if key == "'p'": #this also allows player to pause by pressing 'p'
#         pause_game()
    if pause:
        return #don't run the code below if the game is paused
    more_simultons = set()
    for s in find(lambda t: isinstance(t,Space_ship)):
        m = s.update(key) #the update method may return a missle
        if m!=None:
            more_simultons.add(m)
    simultons |= more_simultons #add any missles fired by the tanks 
    
def pause_game():
    global pause
    if pause:
        controller.the_pause_button["text"] = "Pause"
        pause = False
    else:
        controller.the_pause_button["text"] = "Continue"
        pause = True
        
def reset():
    global first, second, pause, ship, simultons, score, obstacles
    first = True
    second = False
    pause = False
    ship = None #this becomes the space ship that the player controls
    simultons = set() # a set of simultons, starting with the ship
    score = 0
    obstacles = {Asteroid:0.1, Floater:0.01}
        
#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    global simultons
    #deletes all the objects drawn on the canvas
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    #redraws the canvas with objects containing new data    
    for s in simultons:
        s.display(controller.the_canvas)
