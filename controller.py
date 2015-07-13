from tkinter import Button,Label,Canvas

# import model to refer to functions that buttons call via command=...
import model


# The simulation_canvas/progress widgets, when called, set these before they return
# The model uses this information in the world and display_all functions
the_canvas   = None
the_score = None
the_pause_button = None
 
#the initial start screen
def initialize():
    model.start()
    model.display_all()
    
# Buttons/Canvas are called in the view and call methods in the model 
def pause_button  (parent,**config):
    global the_pause_button 
    the_pause_button = Button(parent,command=model.pause_game,**config)
    return the_pause_button

def simulation_canvas  (parent,**config):
    global the_canvas
    the_canvas = Canvas(parent,**config)
    the_canvas.focus_set() #this makes tkinter canvas accept keyboard commands
    the_canvas.bind("<Key>", lambda event: model.move_ship(event))
    return the_canvas


def progress  (parent,**config):
    global the_score
    the_score = Label(parent,**config)
    return the_score


# By the script calling this function, the update_all/display_all in the model
#   is called every 100 milliseconds in the GUI's/root thread, and then this
#   function reschedules itself to be called in 100 milliseconds
# This makes the simulation update itself every .1 seconds
def repeater(root):
    if model.game_over: return #end the game
    model.update_all()
    model.display_all()
    root.after(100,repeater,root)