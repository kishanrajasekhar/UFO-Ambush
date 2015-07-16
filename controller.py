#Code is originally written by Professor Richard Pattis' of
#of University Of Califorina, Irvine. I made some modifications.

#Sets ups all the tkinter tools and their functions

from tkinter import Button,Label,Canvas

# import model to refer to functions that buttons call via command=...
import model


# The simulation_canvas/progress widgets, when called, set these before they return
# The model uses this information in the world and display_all functions
the_canvas   = None
the_score = None
the_pause_button = None
 
def initialize():
    '''The initial start screen'''
    model.start()
    model.display_all()
    
def pause_button  (parent,**config):
    '''Buttons/Canvas are called in the view and call methods in the model '''
    global the_pause_button 
    the_pause_button = Button(parent,command=model.pause_game,**config)
    return the_pause_button

def reset_button (parent, **config):
    '''Pressing this button resets the game'''
    return Button(parent,command=model.reset,**config)

def simulation_canvas  (parent,**config):
    '''Initializes the canvas and sets it up to receive user input.'''
    global the_canvas
    the_canvas = Canvas(parent,**config)
    the_canvas.focus_set() #this makes tkinter canvas accept keyboard commands
    the_canvas.bind("<Key>", lambda event: model.move_ship(event))
    return the_canvas


def progress  (parent,**config):
    '''Shows the player's progress (score)'''
    global the_score
    the_score = Label(parent,**config)
    return the_score



def repeater(root):
    '''By the script calling this function, the update_all/display_all in the model
       is called every 100 milliseconds in the GUI's/root thread, and then this
      function reschedules itself to be called in 100 milliseconds
     This makes the simulation update itself every .1 seconds'''
    model.update_all()
    model.display_all()
    root.after(100,repeater,root)