#Code is originally written by Professor Richard Pattis' of
#of University Of Califorina, Irvine. I made some modifications.

#The view module sets up what is seen on the GUI

from tkinter import Tk,Frame,TOP,LEFT,BOTTOM,RAISED,BOTH

# import controller to call/create widgets and position them in the view
import controller


# Construct a simple root window
root = Tk()
root.title("Simulation")
root.protocol("WM_DELETE_WINDOW",quit)

frame = Frame(root)

# Place buttons simply at the top
frame.pack(side=TOP)
controller.reset_button  (frame,text="Reset")  .pack(side=LEFT)
controller.pause_button  (frame,text="Pause")  .pack(side=LEFT)
controller.progress(frame,text="Score: 0",width=25,relief=RAISED).pack(side=LEFT)


# Place canvas in the space below
controller.simulation_canvas(root,width=500,height=300,bg="black").pack(side=BOTTOM,expand=True,fill=BOTH)